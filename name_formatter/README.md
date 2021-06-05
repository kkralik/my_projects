## name_formatter - purpose

Simple python program designed to recognise first names and change the data format accornigly in an .xlsx file.

If the program recognises 1 first name in the "název účtu" column and 1 other word, it fills full name in
the corresponding colums and adds a commentary to note success (for easy search of all processed data).

If the program fails to do so, it adds a commentary specifying the issue encountered.

### requirements
For running requires files krestni-jmena.txt (list of common Czech first names for recognition)
and ilustrace-jmena-stara.xlsx (with the data to adjust), both in the same direstory.

### output
Reformatted file ilustrace-jmena-nova.xlsx 

### files in this directory:
* README.md - this file, brief description of the program
* name_formatter.py - program file
* krestni-jmena.txt - list of common Czech first names
* ilustrace_jmena-stara.xlsx - original file before changes
* ilustrace_jmena-nova.xlsx - new file created by the program

### translation Czech -> English
Column names
* transakce = transaction code
* datum transakce = date of transaction
* jméno = first name
* příjmení = last name ("Default" is a default value)
* název účtu = account name (should contain the person's name)
* bank.účet = bank account number
* komentář = commentary

Added commentary
* automaticky zpracováno = automatically processed
* program selhal - nesprávný počet slov v názvu účtu = programm failure - incorrect nmber of words in the account name
* program selhal - chybí křestní jméno = program failure - first name missing
* program selhal - dvě křestní jména = program failure - two first names
* program selhal - nepovolený znak v názvu účtu = program failure - illegal character in the account name
