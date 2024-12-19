from django.shortcuts import render
from django.http import JsonResponse
from .models import Coordinate,Contact
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
my_email = "rishi71213@gmail.com"
password = "bowoopqtkinsvbqw"
gmail_server = "smtp.gmail.com"
gmail_port = 587
my_server = smtplib.SMTP(gmail_server,gmail_port)
my_server.ehlo()
my_server.starttls()
my_server.login(my_email,password)

def map_view(request):
    # Fetch all coordinates from the database
    coordinates = Coordinate.objects.values_list('latitude', 'longitude')

    # Convert Decimal values to float
    formatted_coordinates = [
        {"lat": float(coord[0]), "lng": float(coord[1])}
        for coord in coordinates
    ]
    
    return render(request, 'map.html', {'coordinates': formatted_coordinates})


def add_location_view(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON body
            data = json.loads(request.body)
            print("Received Data:", data)  # Debugging

            # Extract latitude, longitude, disaster_type, and description
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            disaster_type = data.get('disaster_type')
            description = data.get('description')

            # Validate the data
            if latitude is None or longitude is None:
                return JsonResponse({'error': 'Latitude and longitude are required.'}, status=400)
            if disaster_type is None or description is None:
                return JsonResponse({'error': 'Disaster type and description are required.'}, status=400)

            # Add the coordinate to the database
            coordinate = Coordinate(
                latitude=latitude,
                longitude=longitude,
                disaster_type=disaster_type,
                description=description
            )
            coordinate.save()
            map_url = "https://www.google.com/maps/dir/?api=1&destination="+str(latitude)+","+str(longitude)
            html_content = f"""
                <html>
                <body style="font-family: Arial, sans-serif; color: #333; margin: 0; padding: 0; background-color: #f4f4f4;">
                    <div style="max-width: 600px; margin: 20px auto; background: #ffffff; border: 1px solid #ddd; border-radius: 10px; overflow: hidden;">
                        <!-- Header Image -->
                        <div style="padding: 20px;">
                            <!-- Disaster Type Heading -->
                            <h2 style="color: #d9534f; text-align: center;">🚨 Disaster Alert: {disaster_type} 🚨</h2>

                            <!-- Description -->
                            <p style="font-size: 16px;">
                                <strong style="color: #d9534f;">Description:</strong><br>
                                <span style="color: #555;">{description}</span>
                            </p>

                            <!-- Location with Map Link -->
                            <p style="font-size: 16px;">
                                <strong style="color: #5bc0de;">Location:</strong><br>
                                <a href="{map_url}" style="color: #0275d8; text-decoration: none; font-weight: bold;">
                                    📍 View on Map
                                </a>
                            </p>

                            <!-- Call to Action Button -->
                            <div style="text-align: center; margin: 30px 0;">
                                <a href="" 
                                   style="display: inline-block; padding: 12px 25px; font-size: 18px; color: #fff; background-color: #28a745; text-decoration: none; border-radius: 5px; font-weight: bold;">
                                   ✅ Register to Help
                                </a>
                            </div>

                            <!-- Footer Note -->
                            <p style="font-size: 14px; color: #777; text-align: center; margin-top: 20px;">
                                Thank you for your support and quick response! 🌟
                            </p>
                        </div>
                    </div>
                </body>
            </html>
            """
            msg = MIMEMultipart("alternative")
            msg["From"] = my_email
            volunteer_emails = []
            volunteers = list(Contact.objects.values())
            for vol in volunteers:
                volunteer_emails.append(vol["email"])
            msg["To"] = ", ".join(volunteer_emails)
            msg["Subject"] = "Disaster Alert!!!"
            msg.attach(MIMEText(html_content, "html"))
            my_server.sendmail(my_email, volunteer_emails, msg.as_string())
            return JsonResponse({'message': 'Location added successfully!'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
        except Exception as e:
            print("Error:", str(e))  # Debugging
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)
def Display(request):
    Disasters = list(Coordinate.objects.values())
    disasters = []
    for d in Disasters:
        map_url = "https://www.google.com/maps/dir/?api=1&destination="+str(d["latitude"])+","+str(d["longitude"])
        type = d["disaster_type"]
        des = d["description"]
        no = d["number_of_volunteers"]
        ele = {"type":type,"description":des,"location": map_url,"members":no}
        disasters.append(ele)
    return render(request, 'dis.html', {'disasters': disasters})
def new_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Validation
        if not name or not email or not phone:
            return render(request, 'volunteer_registration.html', {
                'error': 'All fields are required.'
            })

        try:
            # Save the contact to the database
            contact = Contact(name=name, email=email, phone=phone)
            contact.save()
            return render(request, 'register.html', {
                'success': 'Registration successful!'
            })
        except Exception as e:
            return render(request, 'register.html', {
                'error': str(e)
            })
    else:
        return render(request, 'register.html')

def homePage(request):
    return render(request, 'home.html')


