from .models import CarMake, CarModel

def initiate():
    # CarMake data
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(
            name=data['name'], description=data['description']
        ))

    # CarModel data with additional details
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[0], "color": "Red",
         "price": 35000.00, "fuel_type": "PETROL",
         "transmission": "AUTOMATIC", "dealer_id": 1},
        {"name": "Qashqai", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[0], "color": "Blue",
         "price": 30000.00, "fuel_type": "DIESEL",
         "transmission": "AUTOMATIC", "dealer_id": 1},
        {"name": "XTRAIL", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[0], "color": "White",
         "price": 32000.00, "fuel_type": "HYBRID",
         "transmission": "MANUAL", "dealer_id": 1},
        {"name": "A-Class", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[1], "color": "Black",
         "price": 45000.00, "fuel_type": "PETROL",
         "transmission": "AUTOMATIC", "dealer_id": 2},
        {"name": "C-Class", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[1], "color": "Silver",
         "price": 50000.00, "fuel_type": "ELECTRIC",
         "transmission": "AUTOMATIC", "dealer_id": 2},
        {"name": "E-Class", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[1], "color": "Gray",
         "price": 60000.00, "fuel_type": "DIESEL",
         "transmission": "MANUAL", "dealer_id": 2},
        {"name": "A4", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[2], "color": "Red",
         "price": 42000.00, "fuel_type": "PETROL",
         "transmission": "MANUAL", "dealer_id": 3},
        {"name": "A5", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[2], "color": "Blue",
         "price": 45000.00, "fuel_type": "HYBRID",
         "transmission": "AUTOMATIC", "dealer_id": 3},
        {"name": "A6", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[2], "color": "White",
         "price": 48000.00, "fuel_type": "ELECTRIC",
         "transmission": "AUTOMATIC", "dealer_id": 3},
        {"name": "Sorrento", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[3], "color": "Black",
         "price": 33000.00, "fuel_type": "PETROL",
         "transmission": "MANUAL", "dealer_id": 4},
        {"name": "Carnival", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[3], "color": "Silver",
         "price": 40000.00, "fuel_type": "DIESEL",
         "transmission": "AUTOMATIC", "dealer_id": 4},
        {"name": "Cerato", "type": "Sedan", "year": 2023,
         "car_make": car_make_instances[3], "color": "Gray",
         "price": 25000.00, "fuel_type": "PETROL",
         "transmission": "MANUAL", "dealer_id": 4},
        {"name": "Corolla", "type": "Sedan", "year": 2023,
         "car_make": car_make_instances[4], "color": "Red",
         "price": 28000.00, "fuel_type": "HYBRID",
         "transmission": "AUTOMATIC", "dealer_id": 5},
        {"name": "Camry", "type": "Sedan", "year": 2023,
         "car_make": car_make_instances[4], "color": "Blue",
         "price": 35000.00, "fuel_type": "ELECTRIC",
         "transmission": "AUTOMATIC", "dealer_id": 5},
        {"name": "Kluger", "type": "SUV", "year": 2023,
         "car_make": car_make_instances[4], "color": "White",
         "price": 40000.00, "fuel_type": "DIESEL",
         "transmission": "MANUAL", "dealer_id": 5},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year'],
            color=data['color'],
            price=data['price'],
            fuel_type=data['fuel_type'],
            transmission=data['transmission'],
            dealer_id=data['dealer_id']
        )
