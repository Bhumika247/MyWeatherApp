import tkinter as tk

window = tk.Tk()
window.title("WeatherApp")

myLabel = tk.Label(text="Please put a temperature in Fahrenheit")
myLabel.pack()

fa = tk.Entry()
fa.pack()

#celsius = (fahrenheit - 32)*(5/9)



def enter():
  f = float(fa.get())
  c = (f - 32)*(5/9)

  
  tempLabel = tk.Label(text="The temperature is " + 
  str(round(c,2)) + " Degree Celsius" )
  tempLabel.pack()

  if c>25:
    tempLabelT = tk.Label(text="Too Hot!")
    tempLabelT.pack()
  else:
    tempLabelT = tk.Label(text = "Too cold!")
    tempLabelT.pack()


ok = tk.Button(text="Convert", command=enter)
ok.pack()

window.mainloop()
