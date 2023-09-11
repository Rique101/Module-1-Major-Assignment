# Prompt user to enter word in English
print('Please enter an English word')
english = input('Please enter an English word: ')
print(f'I will give you the French and German translations: {english}')

# Create lists
list_1 = ['hello', 'bonjour', 'hallo']
list_2 = ['yes', 'oui', 'jawohl']
list_3 = ['no', 'non', 'nein']
list_4 = ['yellow', 'jaune', 'gelb']
list_5 = ['dog', 'chien', 'hund']
list_6 = ['table', 'table', 'tisch']
list_7 = ['book', 'livre', 'buchen']

# Check if the word the user entered is in any of the lists
found_translation = False

if english in list_1:
    print('The French translation is', list_1[1])
    print('The German translation is', list_1[2])
    found_translation = True

elif english in list_2:
    print('The French translation is', list_2[1])
    print('The German translation is', list_2[2])
    found_translation = True

elif english in list_3:
    print('The French translation is', list_3[1])
    print('The German translation is', list_3[2])
    found_translation = True

elif english in list_4:
    print('The French translation is', list_4[1])
    print('The German translation is', list_4[2])
    found_translation = True

elif english in list_5:
    print('The French translation is', list_5[1])
    print('The German translation is', list_5[2])
    found_translation = True

elif english in list_6:
    print('The French translation is', list_6[1])
    print('The German translation is', list_6[2])
    found_translation = True

elif english in list_7:
    print('The French translation is', list_7[1])
    print('The German translation is', list_7[2])
    found_translation = True

if not found_translation:
    print(f'The English word "{english}" isn\'t in my vocabulary!')
