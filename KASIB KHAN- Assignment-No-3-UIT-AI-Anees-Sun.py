#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
Create a program that will call a function to generate KE billing details
on the basis of given inputs.
The functions will only call other functions for any processing and only
print return values from calling function.

def bill_main(monthly_units):
    electric_charges=electricity(monthly_units)
    print("electric charges for ", monthly_units, " = ", electric_charges)
    
    uniform_charges=uniform(monthly_units)
    print("electric charges for ", monthly_units, " = ", fuel_charges)
    
    sales_tax=sales_tax(monthly_units)
    print("electric charges for ", monthly_units, " = ", sales_tax)
    
    advance_tax=advance_tax(monthly_units)
    print("electric charges for ", monthly_units, " = ", advance_tax)
    
    tv_fee=tv_fee(monthly_units)
    print("electric charges for ", monthly_units, " = ", "tv_fee")
    
    total=total(electric_charges, uniform_charges, fuel_charges, sales_tax, advance_tax, tv_fee)
    print("electric charges for ", monthly_units, " = ", total)
    


# In[3]:


def variable_charges (monthly_units):
    if monthly_units > 1 and monthly_units < 1:
        v_charges = monthly_units * 9.43
    if monthly_units > 101 and monthly_units < 200:
        v_charges = monthly_units * 17.9566
    if monthly_units > 201 and monthly_units < 300:
        v_charges = monthly_units * 18.84
    if monthly_units > 301 and monthly_units < 400:
        v_charges = monthly_units * 19.76
    return int(v_charges)

def uniform_adj (june_uni_units):
    result = june_uni_units * 0.5715
    return int(result)

def fuel_adj_a(may):
    m = may * 6.8858
    return int(m)

def fuel_adj_b(jun):
    j = jun * 3.0114
    return int(j)
    

def ke_charges (c1, c2, c3, c4):
    result = c1 + c2 + c3 + c4
    return result

def duty (ke_charges):
    result = ke_charges * 0.015
    return int(result)

def sales_tax (ke_charges, duty):
    result = (ke_charges + duty) * 0.17
    return int(result)

def govt_charges (a, b):
    result = a + b
    return int(result)

def total_dues (a, b):
    result = a + b
    return int(result)

aug_user_input = int(input ("Enter Units of Aug: "))
jun_user_input = int(input ("Enter Units of Jul: "))
jun_uni_user_input = int(input ("Enter Units of Jun: "))
may_user_input = int(input ("Enter Units of May: "))


def main_calc(aug, june, jun_uni, may):
    display_a = variable_charges(aug)
    print ("\nVariable Charges is: ", display_a)
    
    display_b = uniform_adj(jun_uni_user_input)
    print ("\nUniform Adjustment is: ", display_b)
    
    display_c = fuel_adj_a(may_user_input)
    print ("\nFuel Adj of May-22 is : ", display_c)
    
    display_d = fuel_adj_b(jun_user_input)
    print ("\nFuel Adj of June-22 is : ", display_d)
    
    display_e = ke_charges(display_a, display_b, display_c, display_d)
    print ("\nTotal KE Charges are: ", display_e)
    
    display_f = duty(display_e)
    print ("\nElectricity Duty: ", display_f)
    
    display_g = sales_tax(display_e, display_f)
    print ("\nSales Tax: ", display_g)

    display_h = govt_charges(display_f, display_g)
    print ("\nTotal Government Charges are: ", display_h)
    
    display_e = total_dues(display_e, display_h)
    print ("\nYour Electricity Charges for the period: ", display_e)

main_calc(aug_user_input, jun_user_input, jun_uni_user_input, may_user_input)


# In[ ]:





# In[ ]:




