/*
Copyright (C) 2018-2019 de4dot@gmail.com

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

using System;
using System.Collections.Generic;
using System.Text;
using Generator.Enums;
using Generator.IO;

namespace Generator.Documentation.Python {
	sealed class PythonDocCommentWriter : DocCommentWriter {
		const string PYTHON_PACKAGE_NAME = "iced_x86";
		readonly IdentifierConverter idConverter;
		readonly bool isInRootModule;
		readonly string typeSeparator;
		readonly StringBuilder sb;
		int summaryLineNumber;
		bool hasColonText;

		static readonly Dictionary<string, string> toTypeInfo = new Dictionary<string, string>(StringComparer.Ordinal) {
			{ "bcd", "bcd" },
			{ "bf16", "bfloat16" },
			{ "f16", "f16" },
			{ "f32", "f32" },
			{ "f64", "f64" },
			{ "f80", "f80" },
			{ "f128", "f128" },
			{ "i8", "i8" },
			{ "i16", "i16" },
			{ "i32", "i32" },
			{ "i64", "i64" },
			{ "i128", "i128" },
			{ "i256", "i256" },
			{ "i512", "i512" },
			{ "u8", "u8" },
			{ "u16", "u16" },
			{ "u32", "u32" },
			{ "u52", "u52" },
			{ "u64", "u64" },
			{ "u128", "u128" },
			{ "u256", "u256" },
			{ "u512", "u512" },
		};

		public PythonDocCommentWriter(IdentifierConverter idConverter, bool isInRootModule, string typeSeparator = ".") {
			this.idConverter = idConverter;
			this.isInRootModule = isInRootModule;
			this.typeSeparator = typeSeparator;
			sb = new StringBuilder();
		}

		string GetStringAndReset() {
			while (sb.Length > 0 && char.IsWhiteSpace(sb[^1]))
				sb.Length--;
			var s = sb.ToString();
			sb.Clear();
			return s;
		}

		static string Escape(string s) {
			s = s.Replace(@"\", @"\\");
			s = s.Replace("`", @"\`");
			s = s.Replace("\"", @"\""");
			s = s.Replace("*", @"\*");
			return s;
		}

		void RawWriteWithComment(FileWriter writer, bool writeEmpty = true) {
			var s = GetStringAndReset();
			if (s.Length == 0 && !writeEmpty)
				return;
			if (summaryLineNumber == 0 && hasColonText) {
				// The first line has type info and it's everything before the colon
				s = ": " + s;
			}
			summaryLineNumber++;
			hasColonText = false;
			if (s.Length == 0)
				writer.WriteLineNoIndent(s);
			else
				writer.WriteLine(s);
		}

		void BeginWrite(FileWriter writer) {
			if (sb.Length != 0)
				throw new InvalidOperationException();
			writer.WriteLine(@"""""""");
		}

		void EndWrite(FileWriter writer) {
			RawWriteWithComment(writer, false);
			writer.WriteLine(@"""""""");
		}

		public void WriteSummary(FileWriter writer, string? documentation, string typeName) {
			if (string.IsNullOrEmpty(documentation))
				return;
			summaryLineNumber = 0;
			hasColonText = false;
			BeginWrite(writer);
			WriteDoc(writer, documentation, typeName);
			EndWrite(writer);
		}

		void Write(string text) =>
			sb.Append(text);

		void WriteDoc(FileWriter writer, string documentation, string typeName) {
			foreach (var info in GetTokens(typeName, documentation)) {
				string t, m;
				switch (info.kind) {
				case TokenKind.NewParagraph:
					if (!string.IsNullOrEmpty(info.value) && !string.IsNullOrEmpty(info.value2))
						throw new InvalidOperationException();
					RawWriteWithComment(writer);
					RawWriteWithComment(writer);
					break;
				case TokenKind.String:
					hasColonText |= info.value.Contains(':', StringComparison.Ordinal);
					sb.Append(Escape(info.value));
					if (!string.IsNullOrEmpty(info.value2))
						throw new InvalidOperationException();
					break;
				case TokenKind.Code:
					sb.Append("``");
					sb.Append(info.value);
					sb.Append("``");
					if (!string.IsNullOrEmpty(info.value2))
						throw new InvalidOperationException();
					break;
				case TokenKind.PrimitiveType:
					if (!toTypeInfo.TryGetValue(info.value, out var type))
						throw new InvalidOperationException($"Unknown type '{info.value}, comment: {documentation}");
					sb.Append("``");
					sb.Append(idConverter.Type(type));
					sb.Append("``");
					if (!string.IsNullOrEmpty(info.value2))
						throw new InvalidOperationException();
					break;
				case TokenKind.Type:
					sb.Append(":class:`");
					if (!isInRootModule && info.value != typeName)
						sb.Append(PYTHON_PACKAGE_NAME + ".");
					t = RemoveNamespace(idConverter.Type(info.value));
					sb.Append(t);
					sb.Append('`');
					if (!string.IsNullOrEmpty(info.value2))
						throw new InvalidOperationException();
					break;
				case TokenKind.EnumFieldReference:
				case TokenKind.FieldReference:
					sb.Append(":class:`");
					WriteTypeName(typeName, info.value);
					if (info.kind == TokenKind.EnumFieldReference) {
						if (PythonUtils.UppercaseEnum(info.value))
							m = info.value2.ToUpperInvariant();
						else
							m = idConverter.EnumField(info.value2);
					}
					else
						m = idConverter.Field(info.value2);
					sb.Append(m);
					sb.Append('`');
					break;
				case TokenKind.Property:
					sb.Append(":class:`");
					WriteTypeName(typeName, info.value);
					m = idConverter.PropertyDoc(info.value2);
					sb.Append(m);
					sb.Append('`');
					break;
				case TokenKind.Method:
					sb.Append(":class:`");
					WriteTypeName(typeName, info.value);
					m = idConverter.MethodDoc(TranslateMethodName(info.value2));
					sb.Append(m);
					sb.Append('`');
					break;
				default:
					throw new InvalidOperationException();
				}
			}
		}

		void WriteTypeName(string thisTypeName, string currentTypeName) {
			if (!isInRootModule && currentTypeName != thisTypeName)
				sb.Append(PYTHON_PACKAGE_NAME + ".");
			if (currentTypeName != thisTypeName) {
				sb.Append(idConverter.Type(currentTypeName));
				sb.Append(typeSeparator);
			}
		}
	}
}
