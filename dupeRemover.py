
with open('scraped.csv','r') as in_file, open('2.csv','w') as out_file:
    seen = set()
    for line in in_file:
        if line in seen: continue

        seen.add(line)
        out_file.write(line)
