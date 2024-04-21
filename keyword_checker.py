import os
directory = "/Users/tenzin/School/INFO1110/Assignment1"
file_ext = ".py"

banned_keywords = [
    "for ", " in ", "__contains__", "global", "lambda", "nonlocal",
    "all(", "any(", "map(", "filter(", "min(",
    "max(", "sum(", " eval(", "exec(", "compile(",
    "sum(", "enumerate(", "global(", "locals("
]

allowed_imports = [
    "sys", "typing", "unittest"
]

banned_imports = []

#adds modules I have written into the allowed imports list
for filename in os.listdir((directory)):
    if filename.endswith(file_ext):
        allowed_imports.append(filename[:-3])

in_docstring = False
for filename in os.listdir(directory):
    if filename.endswith(".py"):
        with open(os.path.join(directory, filename), 'r') as file:
            line_num = 1
            for line in file:
                docstring_count = line.count('"""')
                docstring_count += line.count("'''")
                if docstring_count % 2 == 1:
                    in_docstring = not in_docstring
                if in_docstring: continue
                if line.strip().startswith("#"): continue

                if line.startswith("import") or line.startswith("from"):
                    flag = True
                    for word in line.split():
                        if word in allowed_imports:
                            flag = False
                        if word in banned_imports:
                            print(f"{filename} {line_num}: {line}")
                            continue
                    if flag: print(f"{filename} {line_num}: {line}")
                    continue #so that imports can't set off keywords

                for keyword in banned_keywords:
                    if keyword in line:
                        print(f"{filename} {line_num}: {line}")
                line_num += 1

print("Done searching.")                       
