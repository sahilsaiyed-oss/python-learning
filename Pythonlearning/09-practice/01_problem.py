f = open("poem.txt")
content = f.read()
if("twinkle" in content ):
    print("twinkle is presetnt in the content")

else:
     print("twinkle is not presetnt in the content")
    
f.close()