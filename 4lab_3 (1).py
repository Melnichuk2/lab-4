#14. Дано два упорядкованих за спаданням списки. Об'єднайте їх в новий упорядкований за спаданням
#список.


new1_list = [ 5,32,24,14,7]
new2_list = [ 1,8,56,74,92]
new3_list = new1_list + new2_list
new3_list.sort(reverse = True)
print(new3_list)