source = input("Enter name of source file: ")
with open(source, 'r') as f1:
    target = input("Enter name of target file in which data is going to be copied: ")
    with open(target, 'w') as f2:
        rd_data = f1.read()
        f2.write(rd_data)