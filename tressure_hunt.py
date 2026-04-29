print("""
                 /,   ,|   ,|
             /| /(  ,' / ,//
          \`( |/ /,'  (,/ |
           \ \ ` `   `  /--,
         _,_\ `  ` `  ``  /__
          '-.____________`  /
            [  \@,    :] `--,-..-
            [__________]__,'-._/
             )'o\ ' o) \/ )
             \  /   __  ./
              \=`   ==,\..
               \ -. `,' (333
               3`--''    \33.
             ,333_) /mm33333:.
            |:#:mmmmmm333333::
            |:#:333333333::##'
            ':#:ctr3333''#####\
             |:#:#\###########\
             |:#:##\###########\
             |:#:###\########|#\
             /:#:|:::\|::::::|:(
             ):#:|::::\::::::|:/
            /:#;/:::::<::::::|(
 """)

print("*****WELCOME TO THE TRESSURE ISLAND*****\n your mission is to find the tressure")
a=input("enter left or right:")
if a=="right":
    b=input("wait or swim:")
    if b=="wait":
        c=input("Choose Door Red,Yellow or green:")
        if c=="yellow":
            print("Tressure found....!!******You win******")
        else:
            print("Game over")
    else:
        print("Game over")
else :
    print("Game over")

      
      
