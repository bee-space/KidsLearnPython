import wr

print('Бібліотека')
wr.GetAllWriters()
writerNumber = int(input('Введіть номер письменика про якого хотіли б дізнатись: '))
wr.GetBirthday(writerNumber)
