from django.shortcuts import render
from django.http import JsonResponse
from .models import Coordinate
import json
import smtplib
from email.mime.text import MIMEText
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
            msg = str(disaster_type) + "\n" + str(map_url) + "\n" + str(description)
            msg1 = MIMEText(msg, "plain", "utf-8")
            my_server.sendmail(from_addr=my_email,to_addrs="yushaoffline@gmail.com", msg=msg1.as_string())
            return JsonResponse({'message': 'Location added successfully!'}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
        except Exception as e:
            print("Error:", str(e))  # Debugging
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)



