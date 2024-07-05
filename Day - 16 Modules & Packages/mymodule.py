var1 = 34

def m_add(num1, num2):
	return num1 + num2


def m_sub(xvar, yvar):
	return xvar - yvar


class Person:
	def fun(self):
		print('I am inside class of module')


def m_sqrt(number, precision):
	start = 0
	end, ans = number, 1
	while (start <= end):
		mid = int((start + end) / 2)
		if (mid * mid == number):
			ans = mid
			break
		if (mid * mid < number):
			start = mid + 1
			ans = mid

		else:
			end = mid - 1

	increment = 0.1
	for i in range(0, precision):
		while (ans * ans <= number):
			ans += increment
		ans = ans - increment
		increment = increment / 10
	return ans
