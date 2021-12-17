import pywhatkit as pw

txt = """Python is an interpreted high-level general-purpose programming language.
Its design philosophy emphasizes code readability with its use of significant indentation.
Its language constructs as well as its object-oriented approach aim to help programmers write clear,
logical code for small and large-scale projects."""

pw.text_to_handwriting(txt,"demo.png",[0,0,138])
print("END")
