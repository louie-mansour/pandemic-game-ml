from typing import Dict
from src.models.shared.city import City
from src.models.map.location import Location


class LocationGraph:
    def __init__(self):
        self.locations: Dict[City, Location] = {
            City.ALGIERS: Location(City.ALGIERS),
            City.ATLANTA: Location(City.ATLANTA),
            City.BAGHDAD: Location(City.BAGHDAD),
            City.BANGKOK: Location(City.BANGKOK),
            City.BEIJING: Location(City.BEIJING),
            City.BOGOTA: Location(City.BOGOTA),
            City.BUENOS_AIRES: Location(City.BUENOS_AIRES),
            City.CAIRO: Location(City.CAIRO),
            City.CHENNAI: Location(City.CHENNAI),
            City.CHICAGO: Location(City.CHICAGO),
            City.DELHI: Location(City.DELHI),
            City.ESSEN: Location(City.ESSEN),
            City.HO_CHI_MINH_CITY: Location(City.HO_CHI_MINH_CITY),
            City.HONG_KONG: Location(City.HONG_KONG),
            City.ISTANBUL: Location(City.ISTANBUL),
            City.JAKARTA: Location(City.JAKARTA),
            City.JOHANNESBURG: Location(City.JOHANNESBURG),
            City.KARACHI: Location(City.KARACHI),
            City.KHARTOUM: Location(City.KHARTOUM),
            City.KINSHASA: Location(City.KINSHASA),
            City.KOLKATA: Location(City.KOLKATA),
            City.LAGOS: Location(City.LAGOS),
            City.LIMA: Location(City.LIMA),
            City.LONDON: Location(City.LONDON),
            City.LOS_ANGELES: Location(City.LOS_ANGELES),
            City.MADRID: Location(City.MADRID),
            City.MANILA: Location(City.MANILA),
            City.MELBOURNE: Location(City.MELBOURNE),
            City.MEXICO_CITY: Location(City.MEXICO_CITY),
            City.MIAMI: Location(City.MIAMI),
            City.MILAN: Location(City.MILAN),
            City.MONTREAL: Location(City.MONTREAL),
            City.MOSCOW: Location(City.MOSCOW),
            City.MUMBAI: Location(City.MUMBAI),
            City.NEW_YORK: Location(City.NEW_YORK),
            City.OSAKA: Location(City.OSAKA),
            City.PARIS: Location(City.PARIS),
            City.RIYADH: Location(City.RIYADH),
            City.SAN_FRANCISCO: Location(City.SAN_FRANCISCO),
            City.SANTIAGO: Location(City.SANTIAGO),
            City.SAO_PAULO: Location(City.SAO_PAULO),
            City.SEOUL: Location(City.SEOUL),
            City.SHANGHAI: Location(City.SHANGHAI),
            City.ST_PETERSBURG: Location(City.ST_PETERSBURG),
            City.SYDNEY: Location(City.SYDNEY),
            City.TAIPEI: Location(City.TAIPEI),
            City.TOKYO: Location(City.TOKYO),
            City.WASHINGTON: Location(City.WASHINGTON),
        }

        self.locations[City.SAN_FRANCISCO].add_connections(
            self.locations[City.TOKYO], self.locations[City.MANILA], self.locations[City.LOS_ANGELES], self.locations[City.CHICAGO]
        )
        self.locations[City.TOKYO].add_connections(
            self.locations[City.SEOUL], self.locations[City.SHANGHAI], self.locations[City.OSAKA], self.locations[City.SAN_FRANCISCO]
        )
        self.locations[City.MANILA].add_connections(
            self.locations[City.SAN_FRANCISCO], self.locations[City.TAIPEI], self.locations[City.HONG_KONG], self.locations[City.HO_CHI_MINH_CITY],
            self.locations[City.SYDNEY]
        )
        self.locations[City.LOS_ANGELES].add_connections(
            self.locations[City.SAN_FRANCISCO], self.locations[City.CHICAGO], self.locations[City.MEXICO_CITY], self.locations[City.SYDNEY]
        )
        self.locations[City.CHICAGO].add_connections(
            self.locations[City.SAN_FRANCISCO], self.locations[City.LOS_ANGELES], self.locations[City.MEXICO_CITY], self.locations[City.ATLANTA],
            self.locations[City.MONTREAL]
        )
        self.locations[City.MEXICO_CITY].add_connections(
            self.locations[City.LOS_ANGELES], self.locations[City.CHICAGO], self.locations[City.MIAMI], self.locations[City.LIMA], self.locations[City.BOGOTA]
        )
        self.locations[City.MIAMI].add_connections(
            self.locations[City.ATLANTA], self.locations[City.WASHINGTON], self.locations[City.BOGOTA], self.locations[City.MEXICO_CITY],
            self.locations[City.SAO_PAULO]
        )
        self.locations[City.WASHINGTON].add_connections(
            self.locations[City.ATLANTA], self.locations[City.NEW_YORK], self.locations[City.MONTREAL], self.locations[City.MIAMI]
        )
        self.locations[City.NEW_YORK].add_connections(
            self.locations[City.MONTREAL], self.locations[City.WASHINGTON], self.locations[City.LONDON], self.locations[City.MADRID]
        )
        self.locations[City.MONTREAL].add_connections(
            self.locations[City.CHICAGO], self.locations[City.NEW_YORK], self.locations[City.WASHINGTON]
        )
        self.locations[City.ATLANTA].add_connections(
            self.locations[City.CHICAGO], self.locations[City.MIAMI], self.locations[City.WASHINGTON]
        )

        self.locations[City.MADRID].add_connections(
            self.locations[City.NEW_YORK], self.locations[City.LONDON], self.locations[City.PARIS], self.locations[City.SAO_PAULO],
            self.locations[City.ALGIERS]
        )
        self.locations[City.LONDON].add_connections(
            self.locations[City.NEW_YORK], self.locations[City.MADRID], self.locations[City.PARIS], self.locations[City.ESSEN]
        )
        self.locations[City.PARIS].add_connections(
            self.locations[City.LONDON], self.locations[City.MADRID], self.locations[City.ESSEN], self.locations[City.MILAN], self.locations[City.ALGIERS]
        )
        self.locations[City.ESSEN].add_connections(
            self.locations[City.LONDON], self.locations[City.PARIS], self.locations[City.MILAN], self.locations[City.ST_PETERSBURG]
        )
        self.locations[City.MILAN].add_connections(
            self.locations[City.PARIS], self.locations[City.ESSEN], self.locations[City.ISTANBUL]
        )
        self.locations[City.ST_PETERSBURG].add_connections(
            self.locations[City.ESSEN], self.locations[City.ISTANBUL], self.locations[City.MOSCOW]
        )
        self.locations[City.ALGIERS].add_connections(
            self.locations[City.MADRID], self.locations[City.PARIS], self.locations[City.ISTANBUL], self.locations[City.CAIRO]
        )
        self.locations[City.ISTANBUL].add_connections(
            self.locations[City.ALGIERS], self.locations[City.MILAN], self.locations[City.ST_PETERSBURG], self.locations[City.MOSCOW],
            self.locations[City.BAGHDAD]
        )
        self.locations[City.MOSCOW].add_connections(
            self.locations[City.ST_PETERSBURG], self.locations[City.ISTANBUL]
        )

        self.locations[City.BAGHDAD].add_connections(
            self.locations[City.ISTANBUL], self.locations[City.CAIRO], self.locations[City.RIYADH], self.locations[City.KARACHI]
        )
        self.locations[City.RIYADH].add_connections(
            self.locations[City.BAGHDAD], self.locations[City.CAIRO], self.locations[City.KARACHI]
        )
        self.locations[City.KARACHI].add_connections(
            self.locations[City.MUMBAI], self.locations[City.DELHI], self.locations[City.BAGHDAD], self.locations[City.RIYADH]
        )
        self.locations[City.MUMBAI].add_connections(
            self.locations[City.KARACHI], self.locations[City.DELHI], self.locations[City.CHENNAI]
        )
        self.locations[City.DELHI].add_connections(
            self.locations[City.KARACHI], self.locations[City.MUMBAI], self.locations[City.CHENNAI], self.locations[City.KOLKATA]
        )
        self.locations[City.CHENNAI].add_connections(
            self.locations[City.MUMBAI], self.locations[City.DELHI], self.locations[City.KOLKATA], self.locations[City.BANGKOK],
            self.locations[City.JAKARTA]
        )
        self.locations[City.KOLKATA].add_connections(
            self.locations[City.DELHI], self.locations[City.CHENNAI], self.locations[City.BANGKOK], self.locations[City.HONG_KONG]
        )
        self.locations[City.BANGKOK].add_connections(
            self.locations[City.KOLKATA], self.locations[City.CHENNAI], self.locations[City.HO_CHI_MINH_CITY], self.locations[City.HONG_KONG],
            self.locations[City.JAKARTA]
        )
        self.locations[City.HO_CHI_MINH_CITY].add_connections(
            self.locations[City.BANGKOK], self.locations[City.JAKARTA], self.locations[City.HONG_KONG], self.locations[City.MANILA]
        )
        self.locations[City.JAKARTA].add_connections(
            self.locations[City.SYDNEY], self.locations[City.MANILA], self.locations[City.HO_CHI_MINH_CITY], self.locations[City.BANGKOK]
        )

        self.locations[City.HONG_KONG].add_connections(
            self.locations[City.SHANGHAI], self.locations[City.TAIPEI], self.locations[City.MANILA], self.locations[City.HO_CHI_MINH_CITY],
            self.locations[City.BANGKOK], self.locations[City.SEOUL]
        )
        self.locations[City.SHANGHAI].add_connections(
            self.locations[City.BEIJING], self.locations[City.SEOUL], self.locations[City.TAIPEI], self.locations[City.HONG_KONG],
            self.locations[City.TOKYO]
        )
        self.locations[City.BEIJING].add_connections(
            self.locations[City.SHANGHAI], self.locations[City.SEOUL]
        )
        self.locations[City.SEOUL].add_connections(
            self.locations[City.BEIJING], self.locations[City.SHANGHAI], self.locations[City.TOKYO], self.locations[City.HONG_KONG]
        )
        self.locations[City.TAIPEI].add_connections(
            self.locations[City.SHANGHAI], self.locations[City.HONG_KONG], self.locations[City.OSAKA], self.locations[City.MANILA]
        )
        self.locations[City.OSAKA].add_connections(
            self.locations[City.TOKYO], self.locations[City.TAIPEI]
        )

        self.locations[City.SYDNEY].add_connections(
            self.locations[City.JAKARTA], self.locations[City.MANILA], self.locations[City.LOS_ANGELES]
        )

        self.locations[City.BOGOTA].add_connections(
            self.locations[City.MEXICO_CITY], self.locations[City.LIMA], self.locations[City.MIAMI], self.locations[City.SAO_PAULO],
            self.locations[City.BUENOS_AIRES]
        )
        self.locations[City.LIMA].add_connections(
            self.locations[City.MEXICO_CITY], self.locations[City.BOGOTA], self.locations[City.SANTIAGO]
        )
        self.locations[City.SANTIAGO].add_connections(
            self.locations[City.LIMA]
        )
        self.locations[City.SAO_PAULO].add_connections(
            self.locations[City.BOGOTA], self.locations[City.BUENOS_AIRES], self.locations[City.LAGOS], self.locations[City.MADRID]
        )
        self.locations[City.BUENOS_AIRES].add_connections(
            self.locations[City.BOGOTA], self.locations[City.SAO_PAULO]
        )

        self.locations[City.LAGOS].add_connections(
            self.locations[City.KINSHASA], self.locations[City.KHARTOUM], self.locations[City.SAO_PAULO]
        )
        self.locations[City.KINSHASA].add_connections(
            self.locations[City.LAGOS], self.locations[City.KHARTOUM], self.locations[City.JOHANNESBURG]
        )
        self.locations[City.KHARTOUM].add_connections(
            self.locations[City.CAIRO], self.locations[City.LAGOS], self.locations[City.KINSHASA], self.locations[City.JOHANNESBURG]
        )
        self.locations[City.JOHANNESBURG].add_connections(
            self.locations[City.KINSHASA], self.locations[City.KHARTOUM]
        )
        self.locations[City.CAIRO].add_connections(
            self.locations[City.ALGIERS], self.locations[City.ISTANBUL], self.locations[City.BAGHDAD], self.locations[City.RIYADH],
            self.locations[City.KHARTOUM]
        )
    
    def get_location_by_city(self, city) -> Location:
        return self.locations[city]
