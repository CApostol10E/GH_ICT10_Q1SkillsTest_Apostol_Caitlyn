from pyscript import display, document


 def ordering_form(e):
 item1 = document.getElementById('menu1').value
 item2 = document.getElementById('menu2').value
 item3 = document.getElementById('menu3').value
 item4 = document.getElementById('menu4').value
 item5 = document.getElementById('menu5').value
 item6 = document.getElementById('menu6').value

 total = (float(item1) * menu1.checked + 
          float(item2) * menu2.checked + 
          float(item3) * menu3.checked +
          float(item4) * menu4.checked + 
          float(item5) * menu5.checked +
          float(item6) * menu6.checked)

    display(f'The total amount is {total}', target='output')
    display(f"Your information are {Caitlyn Apostol}")
if your_input.isnumeric():
    print("The input is numeric.")
else:
    print("The input is not numeric.")