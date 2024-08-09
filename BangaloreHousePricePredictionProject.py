## Creating GUI 
from customtkinter import *
import pickle
import joblib

# Load the trained model
model = joblib.load('model.pkl')

# Load the dictionary
with open('variables_dict.pkl', 'rb') as f:
    variables_dict = pickle.load(f)

# Loading Unique_values Dictiorney
with open('unique_val_dic.pkl', 'rb') as f:
    unique_val_dic = pickle.load(f)

def check_fields():
    if (area_dropdown.get() and availability_dropdown.get() and location_dropdown.get() and 
        sizes_dropdown.get() and society_dropdown.get() and SQFT_entry.get() and 
        bath_dropdown.get() and balcony_dropdown.get()):
        submit_button.configure(state='normal', fg_color='blue')
    else:
        submit_button.configure(state='disabled', fg_color='gray')

def on_submit():
    result = []
    for widget in result_frame.winfo_children():
        widget.destroy()
      
    area_type = area_dropdown.get()
    avilability = availability_dropdown.get()
    location = location_dropdown.get()
    sizes = sizes_dropdown.get()
    society = society_dropdown.get()
    total_sqft = SQFT_entry.get()
    bath = bath_dropdown.get()
    balcony = balcony_dropdown.get()
    total_sqft = float(total_sqft)
    
    bath = float(bath)
    balcony = float(balcony)
    
    input_data = [area_type, avilability, location, sizes, society, total_sqft, bath, balcony]

    for i in range(len(input_data)):
        if i == 5:  # total_sqft
            X = input_data[i]
            enc_X = (X - variables_dict['total_sqft'][1]) / (variables_dict['total_sqft'][0] - variables_dict['total_sqft'][1])
            result.append(enc_X)
        elif i == 6:  # bath
            X = input_data[i]
            enc_X = (X - variables_dict['bath'][1]) / (variables_dict['bath'][0] - variables_dict['bath'][1])
            result.append(enc_X)
        elif i == 7:  # balcony
            X = input_data[i]
            enc_X = (X - variables_dict['balcony'][1]) / (variables_dict['balcony'][0] - variables_dict['balcony'][1])
            result.append(enc_X)
        else:
            result.append(variables_dict.get(input_data[i], 0))

    predicted_value = model.predict([result])[0]
    if predicted_value < 0:
        CTkLabel(result_frame, text=f'The model has been trained in a way that it will through negative value which is not true. Please Increase the Total SQFT', text_color='Red', font=('Candara', 15, 'bold')).pack(pady=10)
    else:
        CTkLabel(result_frame, text=f'The Estimated Price Should be {round(predicted_value, 2)}', font=('Candara', 15, 'bold')).pack(pady=10)

root = CTk()

## Setting the geometry of the window
root.geometry('1500x1500')

## setting the light them
root._set_appearance_mode('light')


## adding a main scrollable frame for all the frames
main_frame = CTkScrollableFrame(root, width=1500, height=1500)
main_frame.pack()

## Adding Heading to my GUI
header = CTkLabel(main_frame, text='Bangalore House Prediction', font=('Candara', 30, 'bold'), bg_color= 'transparent').pack(pady=20)
subheader = CTkLabel(main_frame, text='By Shane Rahman', font=('Candara', 15)).pack()



## Creating Div Sections For all the variables
frames = ['area', 'availability', 'location', 'sizes', 'society', 'totalSqft', 'bath', 'balcony']
for frame in frames:
    exec(f"{frame}_frame = CTkFrame(main_frame); {frame}_frame.pack(pady=10)")



## Adding Elements
#area_type dropdown
area_header = CTkLabel(area_frame, text='Choose The Area Type', font=('Candara', 15)).pack()
area_dropdown = CTkComboBox(area_frame, values=unique_val_dic['area_type'], width=200)
area_dropdown.pack()

#Avilability Dropdown
availability_header = CTkLabel(availability_frame, text='Choose The Avilability', font=('Candara', 15)).pack()
availability_dropdown = CTkComboBox(availability_frame, values=unique_val_dic['availability'], width=200)
availability_dropdown.pack()

#Location Dropdown
location_header = CTkLabel(location_frame, text='Choose The Location', font=('Candara', 15)).pack()
location_dropdown = CTkComboBox(location_frame, values=unique_val_dic['location'], width=200)
location_dropdown.pack()

# Sizes Dropdown
sizes_header = CTkLabel(sizes_frame, text='Choose The Size', font=('Candara', 15)).pack()
sizes_dropdown = CTkComboBox(sizes_frame, values=unique_val_dic['Sizes'], width=200)
sizes_dropdown.pack()

#society Dropdown
society_header = CTkLabel(society_frame, text='Choose The Society', font=('Candara', 15)).pack()
society_dropdown = CTkComboBox(society_frame, values=unique_val_dic['society'], width=200)
society_dropdown.pack()

# Total SQFT Entry Box
SQFT_header = CTkLabel(totalSqft_frame, text='Enter the Total_SQFT', font=('Candara', 15)).pack()
SQFT_entry = CTkEntry(totalSqft_frame, width=200)
SQFT_entry.pack()
SQFT_entry.bind('<KeyRelease>', lambda event: check_fields())

# Bath Dropdown
bath_header = CTkLabel(bath_frame, text='Choose The No of Bathrooms', font=('Candara', 15)).pack()
bath_dropdown = CTkComboBox(bath_frame, values=[str(value) for value in unique_val_dic['bath']], width=200)
bath_dropdown.pack()

#Balcony Dropdown
balcony_header = CTkLabel(balcony_frame, text='Choose The No. of Balcony',  font=('Candara', 15)).pack()
balcony_dropdown = CTkComboBox(balcony_frame, values=[str(value) for value in unique_val_dic['balcony']], width=200)
balcony_dropdown.pack()

## Adding Estimate Value Button
submit_button = CTkButton(main_frame, command=on_submit, text='Check Price', state='disabled', fg_color='gray')
submit_button.pack()

# Frame for output
result_frame = CTkFrame(main_frame, width=600, height=10)
result_frame.pack(pady=10)

root.mainloop()
