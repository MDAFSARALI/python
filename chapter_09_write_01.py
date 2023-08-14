f=open('chapter_09_write_01.txt','w')
f.write("Write This all in the new text having name chapter_09_write_01.txt")
f.close()
# Use of appending mode
f=open('chapter_09_write_01.txt','a')
f.write("\nI am appending this.")
f.close()
# If we run this program multiple times then multiolee times appending will occure