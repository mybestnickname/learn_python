import traceback
import sys
try:
    age = int(input('How old are you? '))
    if age < 0:
        raise ValueError
except ValueError:
    print(traceback.format_exc())
    sys.exit('Wrong age.')
if age in range(0, 4):
    print('Карапуз.')
elif age in range(4, 7):
    print('Дет. сад.')
elif age in range(7, 17):
    print('Школьник.')
elif age in range(17, 24):
    print('Студент.')
else:
    print('Работяга.')
