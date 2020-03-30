# Analysis of South African Car Prices
An analysis of the factors correlating with car prices in a dataset of South African car prices.
Dataset created by [Boyd Kane](https://github.com/beyarkay) in the [PurchaseAnalysis](https://github.com/beyarkay/PurchaseAnalysis) repository.

This analysis shows a multiple regression of various features onto the price of a car.
The resulting regression coefficients for each feature were output.

The results were as follows:

```bazaar
dataset shape before cleaning: (28068, 29)
dataset shape after cleaning: (21463, 24)
dataset shape after one hot encodings: (21463, 90)
R^2 value: 0.7234100598364673
coefficients:
+0.35	make_ferrari
+0.30	make_lamborghini
+0.25	engine_power_max_kW
+0.19	make_mclaren
+0.18	year
+0.12	specs_central_locking_keyless (opt activity key)
+0.10	make_mercedes-benz
+0.08	engine_size_l
+0.07	specs_kerb_weight
+0.06	engine_fuel_tank_l
+0.06	make_aston martin
+0.06	specs_central_locking_remote (opt keyless / opt activity key)
+0.04	make_maserati
+0.03	make_volkswagen
+0.03	make_volvo
+0.03	engine_fuel_type_d
+0.02	economy_fuel_consumption_lpkm
+0.02	specs_central_locking_keyless
+0.02	safety_airbag_quantity
+0.02	make_audi
+0.02	make_bentley
+0.01	safety_brake_assist
+0.01	make_porsche
+0.01	specs_central_locking_opt remote
+0.01	specs_doors
+0.01	make_land rover
+0.01	specs_central_locking_keyless start (opt keyless access)
+0.01	engine_transmission_a
+0.01	make_hyundai
+0.01	make_bmw
+0.00	specs_central_locking_✔
+0.00	make_daihatsu
+0.00	engine_fuel_type_-
+0.00	specs_central_locking_key
+0.00	engine_fuel_type_h
+0.00	make_smart
+0.00	make_abarth
+0.00	economy_fuel_range_km
+0.00	safety_driver_airbag
-0.00	safety_EBD
-0.00	make_mini
-0.00	specs_central_locking_remote front
-0.00	economy_CO2_gpkm
-0.00	make_faw
-0.00	specs_central_locking_remote (opt keyless)
-0.00	features_aircon
-0.00	make_citroen
-0.00	make_peugeot
-0.00	make_ssangyong
-0.00	make_lexus
-0.00	safety_passenger_airbag
-0.00	make_kia
-0.00	make_mg
-0.00	make_tata
-0.00	make_jmc
-0.00	make_opel
-0.00	specs_central_locking_remote + keyless start
-0.00	make_chery
-0.01	make_alfa romeo
-0.01	engine_transmission_m
-0.01	make_fiat
-0.01	make_honda
-0.01	make_chrysler
-0.01	specs_central_locking_manual
-0.01	safety_ABS
-0.01	make_chevrolet
-0.01	make_datsun
-0.01	make_mahindra
-0.01	make_jaguar
-0.01	make_subaru
-0.02	specs_seats
-0.02	make_suzuki
-0.02	make_infiniti
-0.02	make_mazda
-0.02	make_jac
-0.02	make_mitsubishi
-0.02	make_gwm
-0.02	make_isuzu
-0.02	make_renault
-0.02	make_dodge
-0.03	features_bluetooth
-0.03	specs_central_locking_remote
-0.03	make_toyota
-0.03	engine_fuel_type_p
-0.03	make_haval
-0.03	make_nissan
-0.04	specs_central_locking_remote (opt keyless start / opt keyless start + access)
-0.04	make_jeep
-0.04	make_ford
-0.15	odometer_km
```

The car make had a large effect on the car price. (understandably)

The car make was then removed and the regression was run again.
The new results were as follows:

```
dataset shape before cleaning: (28068, 28)
dataset shape after cleaning: (21463, 23)
dataset shape after one hot encodings: (21463, 38)
R^2 value: 0.4741135440663866
coefficients:
+0.41	engine_power_max_kW
+0.16	year
+0.11	specs_central_locking_keyless (opt activity key)
+0.10	engine_size_l
+0.06	engine_fuel_tank_l
+0.04	specs_central_locking_remote (opt keyless / opt activity key)
+0.03	safety_airbag_quantity
+0.03	engine_fuel_type_d
+0.03	specs_central_locking_keyless start (opt keyless access)
+0.03	economy_fuel_consumption_lpkm
+0.02	specs_central_locking_opt remote
+0.01	safety_EBD
+0.01	safety_brake_assist
+0.01	engine_transmission_a
+0.01	specs_central_locking_remote front
+0.01	specs_central_locking_✔
+0.00	specs_central_locking_key
+0.00	engine_fuel_type_-
+0.00	specs_central_locking_keyless
+0.00	engine_fuel_type_h
+0.00	safety_driver_airbag
-0.00	specs_central_locking_remote (opt keyless)
-0.00	economy_fuel_range_km
-0.00	specs_kerb_weight
-0.00	features_aircon
-0.00	specs_doors
-0.00	safety_passenger_airbag
-0.00	economy_CO2_gpkm
-0.00	specs_central_locking_remote (opt keyless start / opt keyless start + access)
-0.01	engine_transmission_m
-0.01	specs_central_locking_remote + keyless start
-0.01	specs_central_locking_manual
-0.02	safety_ABS
-0.02	specs_central_locking_remote
-0.03	engine_fuel_type_p
-0.03	features_bluetooth
-0.05	specs_seats
-0.18	odometer_km
```

In the absence of car make information, the engine power appeared to have the largest positive effect on the car price.
The year also had a positive effect on price (as we would expect, since cars depreciate).
The odometer reading had the largest negative effect on price (another expected result since cars typically lose value with mileage).
