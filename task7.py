#погружение в python
#неделя 3 задание 2
#классы и наследование

import csv
import os

class CarBase:
    car_type = None
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
    
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    car_type = 'car'
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = 'truck'
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
        try:
            if (body_whl != ''):
                self.body_length = float(change(self.body_whl[0:self.body_whl.find('x', None, None)]))
                self.body_width = float(change(self.body_whl[self.body_whl.find('x', None,None)+1:self.body_whl.rfind('x', None,None)]))
                self.body_height = float(change(self.body_whl[self.body_whl.rfind('x', None,None)+1:]))
            else:
                self.body_length = float('0')
                self.body_width = float('0')
                self.body_height = float('0')
        except ValueError:
            self.body_length = float('0')
            self.body_width = float('0')
            self.body_height = float('0')
    
    def get_body_volume(self):
        return float(self.body_length) * float(self.body_width) * float(self.body_height)


class SpecMachine(CarBase):
    car_type = 'spec_machine'
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
      
      
def change(s):
    if s == '':
        return s.replace('', '0')
    else:
        return s
      
def get_car_list(csv_filename):
    cars = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for r in reader:
            if len(r) < 6:
                continue
            elif (r[0] != '') and (r[1] != '') and (r[3] != '') and (r[5] != '') and (r[5][0:r[5].find('.', None, None)] != ''):
                if (r[0] == 'car'):
                    try:
                        cr = Car(str(r[1]), str(r[3]), str(r[5]), str(r[2]))
                        if (cr.get_photo_file_ext() == '.jpg') or (cr.get_photo_file_ext() == '.jpeg') or (cr.get_photo_file_ext() == '.png') or (cr.get_photo_file_ext() == '.gif'):
                                cars.append(cr)
                    except ValueError:
                        pass
                elif (r[0] == 'truck'):
                    try:
                        tr = Truck(str(r[1]), str(r[3]), str(r[5]), str(r[4]))
                        if (tr.get_photo_file_ext() == '.jpg') or (tr.get_photo_file_ext() == '.jpeg') or (tr.get_photo_file_ext() == '.png') or (tr.get_photo_file_ext() == '.gif'):
                                cars.append(tr)
                    except ValueError:
                        pass
                elif (r[0] == 'spec_machine'):
                    try:
                        if (r[6] != ''):
                            sp = SpecMachine(str(r[1]), str(r[3]), str(r[5]), str(r[6]))
                            if (sp.get_photo_file_ext() == '.jpg') or (sp.get_photo_file_ext() == '.jpeg') or (sp.get_photo_file_ext() == '.png') or (sp.get_photo_file_ext() == '.gif'):
                                cars.append(sp)
                        elif (r[6] == ''):
                            pass
                    except ValueError:
                        pass
    return cars