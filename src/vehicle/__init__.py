# -*- coding: utf-8 -*-

from random import choice
from faker.providers import BaseProvider
from .vehicle_dict import vehicles
from .wmi import vehicle_wmi
from .machine_dict import machinery

class VehicleProvider(BaseProvider):
    """
    A Provider for vehicle related test data.

    >>> from faker import Faker
    >>> from faker_vehicle import VehicleProvider
    >>> fake = Faker()
    >>> fake.add_provider(VehicleProvider)
    """
    
    def _vin(self, vehicle) -> str:
        """
        Return a VIN for the given vehicle.
        
        VIN is a 17 character string encoding all kinds of information. The World 
        Manufacturer Identifier (WMI) is [0:2], the Vehicle Descriptor Section (VDS) 
        is [3:8], and the Vehicle Identifier Section (vis) is [9:16].
        """
        # TODO: Implement robust WMI association
        wmis = vehicle_wmi.get(vehicle.get('Make')) or vehicle_wmi.get(vehicle.get('Make').title()) or vehicle_wmi.get(vehicle.get('Make').upper())
        if wmis:
            wmi = choice(wmis)
        else:
            return ''
        
        # Position 9 is a check digit in North America and China, but not Europe.
        vds = self.bothify(text='??####')
        
        # Position 9 is the year of manufacture as a single character value starting in 1980.
        letters = 'ABCDEFGHJKLMNPRSTVWXY123456789'
        veh_year = vehicle.get('Year') - 1979
        if veh_year > len(letters):
            veh_year = veh_year - len(letters)
        year = letters[veh_year-1]
        
        # In North America and China position 10 is the plant code.
        plant = 'A'
        
        # Remaining portion is the serial number
        serial = self.numerify(text='######')
        
        vis = ''.join([year, plant, serial])
        
        return ''.join([wmi, vds, vis])

    def vehicle_object(self):
        """
        Returns a random vehicle dict example:
        {"Year": 2008, "Make": "Jeep", "Model": "Wrangler", "Category": "SUV"}
        """
        veh = choice(vehicles)
        
        veh['VIN'] = self._vin(veh)
        
        return veh
    
    def vehicle_vin(self):
        """Returns a VIN."""
        veh = self.vehicle_object()
        return veh.get('VIN')

    def vehicle_year_make_model(self):
        """Returns Year Make Model example: 1997 Nissan 240SX"""
        veh = self.vehicle_object()
        year = veh.get('Year')
        make = veh.get('Make')
        model = veh.get('Model')
        return str(year) + ' ' + make + ' ' + model

    def vehicle_year_make_model_cat(self):
        """
        Returns Year Make Model Cat example:
        2017 GMC Sierra 1500 Double Cab (Pickup)
        """
        veh = self.vehicle_object()
        year = veh.get('Year')
        make = veh.get('Make')
        model = veh.get('Model')
        cat = veh.get('Category')
        return str(year) + ' ' + make + ' ' + model + ' (' + cat + ')'

    def vehicle_make_model(self):
        """Returns Make Model example: Audi Q7"""
        veh = self.vehicle_object()
        make = veh.get('Make')
        model = veh.get('Model')
        return make + ' ' + model

    def vehicle_make(self):
        """Returns Make example: Lincoln"""
        veh = self.vehicle_object()
        return veh.get('Make')

    def vehicle_year(self):
        """Returns Year example: 1999"""
        veh = self.vehicle_object()
        return str(veh.get('Year'))

    def vehicle_model(self):
        """Returns Model example: Frontier King Cab"""
        veh = self.vehicle_object()
        return veh.get('Model')

    def vehicle_category(self):
        """Returns Category example: SUV"""
        veh = self.vehicle_object()
        return veh.get('Category')

    def machine_object(self):
        """
        Returns a random machine dict example:
        {"Year": 2008, "Make": "Caterpillar", "Model": "5511C", "Category": "Feller Buncher"}
        """
        machine = choice(machinery)
        return machine

    def machine_year_make_model(self):
        """Returns Year Make Model example: 2008 Caterpillar 5511C"""
        machine = self.machine_object()
        year = machine.get('Year')
        make = machine.get('Make')
        model = machine.get('Model')
        return str(year) + ' ' + make + ' ' + model

    def machine_year_make_model_cat(self):
        """
        Returns Year Make Model Cat example:
        2008 Caterpillar 5511C (Feller Buncher)
        """
        machine = self.machine_object()
        year = machine.get('Year')
        make = machine.get('Make')
        model = machine.get('Model')
        cat = machine.get('Category')
        return str(year) + ' ' + make + ' ' + model + ' (' + cat + ')'

    def machine_make_model(self):
        """Returns Make Model example: Caterpillar 5511C"""
        machine = self.machine_object()
        make = machine.get('Make')
        model = machine.get('Model')
        return make + ' ' + model

    def machine_make(self):
        """Returns Make example: Caterpillar"""
        machine = self.machine_object()
        return machine.get('Make')

    def machine_year(self):
        """Returns Year example: 2008"""
        machine = self.machine_object()
        return str(machine.get('Year'))

    def machine_model(self):
        """Returns Model example: 5511C"""
        machine = self.machine_object()
        return machine.get('Model')

    def machine_category(self):
        """Returns Category example: Feller Buncher"""
        machine = self.machine_object()
        return machine.get('Category')
