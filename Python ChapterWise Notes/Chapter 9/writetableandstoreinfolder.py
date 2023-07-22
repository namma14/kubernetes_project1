# write tables from 2 to 20 and store them in differents files under a folder
for n in range (2,21):
    with open(f"tables/Multiplicaiton_Table_of_{n}",'w') as f:
        for i in range (1,11):
            f.write(f" {n} * {i} = {n*i} \n")
