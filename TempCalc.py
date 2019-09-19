import time;
def Retry():
	time.sleep(1)
	Retry = input("\n\n\n\n\n\nDo you want to calculate again? (Y or 1 to do it again, anything else will exit the calculator)\n") 
	if Retry == "Y" or Retry == "1" or Retry == "y" or Retry == "yes" or Retry == "Yes" or Retry == "yEs" or Retry == "yeS" or Retry == "YEs" or Retry == "YeS" or Retry == "yES" or Retry == "YES":
		TempCalc()
	else:
		quit()

def TempCalc():
	print("Temperature Calculator")
	C = 100
	R = 80
	F = 212
	K = 373.15
	Ra = 671.64
	time.sleep(5)
	print("C " + repr(C) + ":" + "R " + repr(R) + ":" + "F " + repr(F) + ":" + "K " + repr(K) + ":" + "Ra " + repr(Ra) )
	FValue = input("Please input what temperature you want to convert\n" )
	if FValue in ("C", "F", "R", "K", "Ra"):
		FValue2 = input("Please input what temperature you want to convert to\n")
		if FValue2 in ("C", "F", "R", "K", "Ra") and FValue2 != FValue:
			FValue3 = float(input("Please input the temperature number\n"))
			try:
				if FValue == "C":
					if FValue2 == "F":
						Result = FValue3 * 1.8 + 32
						print( repr(FValue3) + " °Celcius converted to Fahrenheit is " + repr(Result) + "°F")
						Retry()
					elif FValue2 == "R":
						Result = FValue3 * 0.8
						print( repr(FValue3) + " °Celcius converted to Reaumur is " + repr(Result) + "°R")
						Retry()
					elif FValue2 == "K":
						Result = FValue3 + 273.15
						print( repr(FValue3) + " °Celcius converted to Kelvin is " + repr(Result) + "°K")
						Retry()
					elif FValue2 == "Ra":
						Result = FValue3 * 1.8 + 32 + 459.67
						print( repr(FValue3) + " °Celcius converted to Rankine is " + repr(Result) + "°Ra")
						Retry()
				elif FValue == "F":
					if FValue2 == "C":
						Result = (FValue3 - 32) / 1.8
						print( repr(FValue3) + " °Fahrenheit converted to Celcius is " + repr(Result) + "°C")
						Retry()
					elif FValue2 == "R":
						Result = (FValue3 - 32) / 2.25
						print( repr(FValue3) + " °Fahrenheit converted to Reaumur is " + repr(Result) + "°R")
						Retry()
					elif FValue2 == "K":
						Result = (FValue3 + 459.67) / 1.8
						print( repr(FValue3) + " °Fahrenheit converted to Kelvin is " + repr(Result) + "°K")
						Retry()
					elif FValue2 == "Ra":
						Result = FValue3 + 459.67
						print( repr(FValue3) + " °Fahrenheit converted to Rankine is " + repr(Result) + "°Ra")
						Retry()
				elif FValue == "R":
					if FValue2 == "C":
						Result = FValue3 * 1.25
						print( repr(FValue3) + " °Reaumur converted to Celcius is " + repr(Result) + "°C")
						Retry()
					elif FValue2 == "F":
						Result = FValue3 * 2.25 + 32
						print( repr(FValue3) + " °Reaumur converted to Fahrenheit is " + repr(Result) + "°F")
						Retry()
					elif FValue2 == "K":
						Result = FValue3 * 1.25 + 273.15
						print( repr(FValue3) + " °Reaumur converted to Kelvin is " + repr(Result) + "°K")
						Retry()
					elif FValue2 == "Ra":
						Result = FValue3 * 2.25 + 32 + 459.67
						print( repr(FValue3) + " °Reaumur converted to Rankine is " + repr(Result) + "°Ra")
						Retry()
				elif FValue == "K":
					if FValue2 == "C":
						Result = FValue3 - 273.15
						print( repr(FValue3) + " °Kelvin converted to Celcius is " + repr(Result) + "°C")
						Retry()
					elif FValue2 == "F":
						Result = FValue3 * 1.8 - 459.67
						print( repr(FValue3) + " °Kelvin converted to Fahrenheit is " + repr(Result) + "°F")
						Retry()
					elif FValue2 == "R":
						Result = (FValue3 - 273.15) * 0.8
						print( repr(FValue3) + " °Kelvin converted to Reaumur is " + repr(Result) + "°R")
						Retry()
					elif FValue2 == "Ra":
						Result = FValue3 * 1.8
						print( repr(FValue3) + " °Kelvin converted to Rankine is " + repr(Result) + "°Ra")
						Retry()
				elif FValue == "Ra":
					if FValue2 == "C":
						Result = (FValue3 - 32 - 459.67) / 1.8
						print( repr(FValue3) + " °Rankine converted to Celcius is " + repr(Result) + "°C")
						Retry()
					elif FValue2 == "F":
						Result = FValue3 - 459.67
						print( repr(FValue3) + " °Rankine converted to Fahrenheit is " + repr(Result) + "°F")
						Retry()
					elif FValue2 == "R":
						Result = (FValue3 - 32 - 459.67) / 2.25
						print( repr(FValue3) + " °Rankine converted to Reaumur is " + repr(Result) + "°R")
						Retry()
					elif FValue2 == "K":
						Result = FValue3 / 1.8
						print( repr(FValue3) + " °Rankine converted to Kelvin is " + repr(Result) + "°K")
						Retry()
			except ValueError:
				print("\nwhat\n")
				TempCalc()
		elif FValue2 in ("C", "F", "R", "K", "Ra") and FValue2 == FValue:
			print("\nTemperature must not be same!")
			TempCalc()
		else:
			print("\nNo")
			TempCalc()

TempCalc()




