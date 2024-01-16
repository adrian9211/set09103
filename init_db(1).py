import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO notes (content,user_id) VALUES (?,?)", ('<h1>Get Started</h1>  This is a simple website that allows you to take notes in Markdown language. Markdown is a lightweight markup language that makes it easy to format text with simple syntax.', 1))
cur.execute("INSERT INTO notes (content,user_id) VALUES (?,?)", ('<h1> Markdown Notepad Quick Guide</h1> <br> <h1>Headers</h1> <br> `# Header 1` <br> `## Header 2`  <br> `### Header 3`  <h1>Emphasis</h1> `*italic* or _italic_` <br> `**bold** or __bold__`  <h1>Lists</h1> `- Item 1` <br> `- Item 2` <br> ` - Subitem 2.1` <br> `- Subitem 2.2`  <h1>Ordered Lists</h1> `1. First item` <br> `2. Second item` <h1>Links</h1> ```[Link Text](https://www.example.com)``` <h1>Images</h1> ```![Alt Text](image-url.jpg)``` <h1>Blockquotes</h1> ```> This is a blockquote.``` <h1>Code</h1> `Inline code: `code <br> Code block: <br> ``` <br>``` Your code ``` <br> ```<h1>Horizotal rule</h1> ``` --- ```<h1>Tables</h1> `| Header 1 | Header 2 |`<br>`|----------|----------|`<br>`| Row 1, Col 1 | Row 1, Col 2 |`<br>`| Row 2, Col 1 | Row 2, Col 2 |` ', 1))
cur.execute("INSERT INTO notes (content,user_id) VALUES (?,?)", ('<h1>Source</h1> <br> For more detailed information, refer to the  [Markdown Guide](https://www.example.com).', 1))

connection.commit()
connection.close()


# Header 1
## Header 2
### Header 3
