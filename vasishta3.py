#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 18:33:39 2023

@author: vasisht
"""


class Employee():
    
    DEFAULT_NAME = "George"
    MIN_VALUE = 1
    MAX_VALUE = 99999999
    BENEFITS_NUMBER = 500
    DEFAULT_EMPLOYEE_NUM = 12345678
    RETURN_CHAR = "\n"
    
    def __init__(self, employee_name, employee_number):
        """
        This is a constructor for class Employee
        pre: takes in employee_name which is a string under 20 characters and
             employee_number which is less than 8 digits
        post: none
        """
        self.set_employee_name(employee_name)
        self.set_employee_number(employee_number)
        

    def get_employee_name(self):
        """
        This function prints the Employee name
        pre: none
        post: returns employee_name as a string of 20 or less characters

        """
        return self._employee_name
     

    def set_employee_name(self, employee_name):
        '''
        This method sets the employee name
        pre: takes the string employee_name of length less than 20 characters
        post: none

        '''
        if (employee_name == ""):
            self._employee_name = self.DEFAULT_EMPLOYEE_NAME
        elif (len(employee_name) >= 20):
            print("Employee name is too long.")
        else:
            self._employee_name = employee_name
            
         

    def get_employee_number(self):
        """
        This function returns the employee number of the Employee.
        pre: none
        post: returns employee_number as a number with 8 digits

        """
        return self._employee_number
    

    def set_employee_number(self, employee_number):
        '''
        This method sets the employee number
        pre: takes the string employee_number with 8 digits exactly
        post: none

        '''
        if (employee_number > self.MIN_VALUE and \
            employee_number < self.MAX_VALUE):
            self._employee_number = employee_number
        else:
            self._employee_number = self.DEFAULT_EMPLOYEE_NUM
            print("Employee Number out of range",employee_number)



    def __str__(self):
        """
        This function pritns all the fiels of the Employee
        pre: none
        post: returns all the fiels of the Employee Name and Employee Number
        """
        output_str = ""
        output_str += "Employee Name: " + str(self.get_employee_name()) + self.RETURN_CHAR
        output_str += "Employee Number: " + '{:0=8}'.format(self.get_employee_number()) + self.RETURN_CHAR
        return output_str

    
class ProductionWorker(Employee):
    DAY_SHIFT = 1
    NIGHT_SHIFT = 2
    MIN_HOURLY_PAY_RATE = 3.00
    MAX_HOURLY_PAY_RATE = 19.99
    DEFAULT_HOURLY_PAY_RATE = 3.01
    DEFAULT_SHIFT = 1
    

    def __init__(self, employee_name, employee_number, shift_number, pay_rate):
        """
        This is a constructor for subclass ProductionWorker
        pre: takes in employee_name which is a string under 20 characters and
             employee_number which is less than 8 digits, shift_number, and
             pay_rate
        post: none
        """
        super().__init__(employee_name, employee_number)
        self.set_shift_number(shift_number)
        self.set_hourly_pay_rate(pay_rate)
        

    def get_hourly_pay_rate(self):
        """
        This function prints the hourly pay rate of the ProductionWorker
        pre: none
        post: returns hourly_pay_rate

        """
        return self._hourly_pay_rate
    

    def set_hourly_pay_rate(self, pay_rate):
        '''
        This function sets the hourly pay rate of the ProductionWorker
        pre: takes the hourly_pay_rate as an integer 
        post: none

        '''
        if (pay_rate > self.MIN_HOURLY_PAY_RATE and \
            pay_rate < self.MAX_HOURLY_PAY_RATE):
            self._hourly_pay_rate = pay_rate
        else:
            self._hourly_pay_rate = self.DEFAULT_HOURLY_PAY_RATE
            
 
    def get_shift_number(self):
        """
        This function returns the shfit number of the ProductionWorker
        pre: none
        post: returns the shift_number

        """
        return self._shift_number
        

    def set_shift_number(self, shift_number):
        '''
        This function sets the shift number of the ProductionWorker
        pre: takes the shift_number as an integer
        post: none

        '''
        if (shift_number != self.DAY_SHIFT and \
            shift_number != self.NIGHT_SHIFT):
            self._shift_number = self.DEFAULT_SHIFT
        else:
            self._shift_number = shift_number
    

    def __str__(self):
        """
        This function returns all the fields of the ProductionWorker
        pre: none
        post: returns all the fiels of the Production Worker
        """
        print("Demo Production Worker:" + self.RETURN_CHAR)
        output_str = super().__str__()    
        output_str += "Enter the shift number: " + str(self.get_shift_number()) + self.RETURN_CHAR
        output_str += "Enter the hourly pay rate: " +str(self.get_hourly_pay_rate()) + self.RETURN_CHAR
        return output_str
    
class ShiftSupervisor(Employee):
    
    def __init__(self, employee_name, employee_number, salary, bonus):
        """
        This is a constructor for subclass ShiftSupervisor
        pre: takes in employee_name which is a string under 20 characters and
             employee_number which is less than 8 digits, salary, and bonus
        post: none
        """
        super().__init__(employee_name, employee_number)
        self.set_salary(salary)
        self.set_bonus(bonus)
        
    def get_salary(self):
        """
        This function prints the salary of the ShiftSupervisor
        pre: none
        post: returns the salary

        """
        return self._salary
    
    def set_salary(self, salary):
        '''
        This function sets the salary of the ShiftSupervisor
        pre: takes the salary as an integer
        post: none

        '''
        self._salary = salary
            
    def get_bonus(self):
        """
        This function prints the bonus of the ShiftSupervisor
        pre: none
        post: returns the bonus

        """
        return self._bonus
        
    def set_bonus(self, bonus):
        '''
        This function sets the bouns of the ShiftSupervisor
        pre: takes the bonus as an integer
        post: none

        '''
        self._bonus = bonus
        
   
    def __str__(self):     
        """
        This function provides all the fields of the class ShiftSupervisor as a string
        pre: none
        post: returns all the fields of the Shift Supervisor
        """
        print("Shift supervisor worker information:" + self.RETURN_CHAR)
        output_str = super().__str__()
        output_str += "Annual Salary:: " + "$"+ '{:,}'.format(self.get_salary())+ \
            self.RETURN_CHAR
        output_str += "Annual Production Bonus: " + "$"+'{:,}'.format(self.get_bonus()) \
            + self.RETURN_CHAR
        return output_str
        
        

        
            
            
        
        
            
   