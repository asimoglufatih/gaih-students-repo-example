#These cv`s are taken from The Sopranos Series.

cvs = {

       'cv1' : {'name': "Anthony",
              'surname': "Soprano",
              'title': "Boss",
              'age': "42"},

       'cv2' : {'name' : "Carmela",
              'surname': "Soprano",
              'title' : "housewife",
              'age' : "38"},
    
       'cv3' : {'name' : "Paulie",
              'surname': "Gualtieri",
              'title' : "caporegime",
              'age' : "60"},

       'cv4' : {'name' : "Silvio",
              'surname' : "Dante",
              'title' : "Consigliere",
              'age' : "52"},


       'cv5' : {'name' : "Arthur",
              'surname' : "Bucco",
              'title' : "restaurateur",
              'age' : "39"}
      

}

for k,v in cvs.items():
    print(f'{k} = ')
    for key, value in v.items():
           print(f'{key} : {value}')
