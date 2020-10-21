def task411(string):
    strList = string.split()
    result = ''
    for word in strList:
        if len(word) > 5:
            result += word + ' '
    return result

str = "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quisquam vitae distinctio rem eum quam velit cum ab voluptatum quas quaerat, nisi corporis suscipit odio? Autem possimus voluptatem rerum culpa animi veniam fugit illum? Asperiores odit aliquid aperiam nobis itaque expedita tenetur iste aliquam ea inventore recusandae eos, cum, corporis ab iusto. Velit nulla tenetur ut minima fugiat aperiam cupiditate dignissimos tempora enim! Dicta esse explicabo reprehenderit repellat numquam exercitationem suscipit asperiores ab velit deleniti adipisci eaque placeat, sapiente eos officia debitis, delectus provident voluptas nesciunt ratione veniam? Tenetur provident officia ipsum rem doloremque impedit aliquid. Amet maiores obcaecati ratione cum!"

print(str)
print()
print(task411(str))
