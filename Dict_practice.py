# Dictionary practice

status = input('Where are you ')
status = status.lower()
Data_MCS = {
    'PS': [{'Nama': 'Adnan', 'Tinggal': status},
           {'Nama': 'Yoga', 'Tinggal': status},
           {'Nama': 'Rezky', 'Tinggal': status},
           {'Nama': 'Suriansyah', 'Tinggal': status},
           {'Nama': 'Edwin', 'Tinggal': status},
           {'Nama': 'Dimas', 'Tinggal': status}],
    'Teknisi': [{'Nama': 'Jay', 'Tinggal': 'M1'},
                {'Nama': 'Diki', 'Tinggal': 'M1'},
                {'Nama': 'Ogi', 'Tinggal': 'Rumah'},
                {'Nama': 'Fikri', 'Tinggal': 'Kos'},
                {'Nama': 'Rangga', 'Tinggal': 'M1'},
                {'Nama': 'Gofur', 'Tinggal': 'M1'}]

}
T = "in"
for stat in range (len(Data_MCS['PS'])):
    if T in (Data_MCS['PS'][stat]['Tinggal']):
        print("sss")

"""
if T in (Data_MCS['PS'][0]['Tinggal']):
    print(f"{Data_MCS['PS'][0]['Nama']} available, segera berangkat!")
else:
    print('Next person please!')
"""