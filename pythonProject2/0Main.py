import os

main_dir = os.getcwd()
os.chdir('pythonProject2/')

exec(open('data_updated.py').read())
exec(open('Datacleaning.py').read())

exec(open('Bars.py').read())
exec(open('Bars_integratedpolicy.py').read())
exec(open('Bars_Date_county.py').read())

exec(open('Emergency.py').read())
exec(open('Emergency_integratedpolicy.py').read())
exec(open('Emergency_date_county.py').read())

exec(open('Gathering.py').read())
exec(open('Gathering_integratedpolicy.py').read())
exec(open('Gathering_Date_county.py').read())

exec(open('Gyms.py').read())
exec(open('Gyms_integratedpolicy.py').read())
exec(open('Gyms_Date_county.py').read())

exec(open('masks_employees.py').read())
exec(open('masks_employees_integratedpolicy.py').read())
exec(open('masks_employees_date_county.py').read())

exec(open('masks_residents.py').read())
exec(open('masks_residents_integratedpolicy.py').read())
exec(open('masks_residents_date_county.py').read())

exec(open('Medical_Nursing_home_covidpositive.py').read())
exec(open('medical_nursinghome_covidpositive_integratedpolicy.py').read())
exec(open('Medical_nursinghome_covidpositive_Date_county.py').read())

exec(open('Medical_Nursing_home_visitors.py').read())
exec(open('medical_nursinghome_visitors_integratedpolicy.py').read())
exec(open('Medical_nursinghome_visitors_Date_county.py').read())

exec(open('Movie.py').read())
exec(open('movie_integratedpolicy.py').read())
exec(open('Movie_Date_county.py').read())

exec(open('no_elective.py').read())
exec(open('no_elective_integratedpolicy.py').read())
exec(open('no_elective_Date_county.py').read())

exec(open('Recreation_beach.py').read())
exec(open('recreation_beach_integratedpolicy.py').read())
exec(open('Recreation_Beach_Date_county.py').read())

exec(open('Recreation_park.py').read())
exec(open('recreation_park_integratedpolicy.py').read())
exec(open('Recreation_Park_Date_county.py').read())

exec(open('Restaurants.py').read())
exec(open('Restaurants_integratedpolicy.py').read())
exec(open('Restaurants_Date_county.py').read())

exec(open('Retail.py').read())
exec(open('Retail_integratedpolicy.py').read())
exec(open('Retail_Date_county.py').read())

exec(open('Spas.py').read())
exec(open('Spas_integratedpolicy.py').read())
exec(open('Spas_Date_county.py').read())

exec(open('Stayhome.py').read())
exec(open('Stayhome_integratedpolicy.py').read())
exec(open('Stayhome_Date_county.py').read())

os.chdir(main_dir)
