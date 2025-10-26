from typing import Dict
from src.models.shared.city import City
from src.models.map.location import Location


class LocationGraphFactory:
    @staticmethod
    def create_location_graph() -> Dict[City, Location]:
        """Create and return a graph of locations with their connections."""
        locations: Dict[City, Location] = {
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

        locations[City.SAN_FRANCISCO].add_connections(
            locations[City.TOKYO], locations[City.MANILA], locations[City.LOS_ANGELES], locations[City.CHICAGO]
        )
        locations[City.TOKYO].add_connections(
            locations[City.SEOUL], locations[City.SHANGHAI], locations[City.OSAKA], locations[City.SAN_FRANCISCO]
        )
        locations[City.MANILA].add_connections(
            locations[City.SAN_FRANCISCO], locations[City.TAIPEI], locations[City.HONG_KONG], locations[City.HO_CHI_MINH_CITY],
            locations[City.SYDNEY]
        )
        locations[City.LOS_ANGELES].add_connections(
            locations[City.SAN_FRANCISCO], locations[City.CHICAGO], locations[City.MEXICO_CITY], locations[City.SYDNEY]
        )
        locations[City.CHICAGO].add_connections(
            locations[City.SAN_FRANCISCO], locations[City.LOS_ANGELES], locations[City.MEXICO_CITY], locations[City.ATLANTA],
            locations[City.MONTREAL]
        )
        locations[City.MEXICO_CITY].add_connections(
            locations[City.LOS_ANGELES], locations[City.CHICAGO], locations[City.MIAMI], locations[City.LIMA], locations[City.BOGOTA]
        )
        locations[City.MIAMI].add_connections(
            locations[City.ATLANTA], locations[City.WASHINGTON], locations[City.BOGOTA], locations[City.MEXICO_CITY],
            locations[City.SAO_PAULO]
        )
        locations[City.WASHINGTON].add_connections(
            locations[City.ATLANTA], locations[City.NEW_YORK], locations[City.MONTREAL], locations[City.MIAMI]
        )
        locations[City.NEW_YORK].add_connections(
            locations[City.MONTREAL], locations[City.WASHINGTON], locations[City.LONDON], locations[City.MADRID]
        )
        locations[City.MONTREAL].add_connections(
            locations[City.CHICAGO], locations[City.NEW_YORK], locations[City.WASHINGTON]
        )
        locations[City.ATLANTA].add_connections(
            locations[City.CHICAGO], locations[City.MIAMI], locations[City.WASHINGTON]
        )

        locations[City.MADRID].add_connections(
            locations[City.NEW_YORK], locations[City.LONDON], locations[City.PARIS], locations[City.SAO_PAULO],
            locations[City.ALGIERS]
        )
        locations[City.LONDON].add_connections(
            locations[City.NEW_YORK], locations[City.MADRID], locations[City.PARIS], locations[City.ESSEN]
        )
        locations[City.PARIS].add_connections(
            locations[City.LONDON], locations[City.MADRID], locations[City.ESSEN], locations[City.MILAN], locations[City.ALGIERS]
        )
        locations[City.ESSEN].add_connections(
            locations[City.LONDON], locations[City.PARIS], locations[City.MILAN], locations[City.ST_PETERSBURG]
        )
        locations[City.MILAN].add_connections(
            locations[City.PARIS], locations[City.ESSEN], locations[City.ISTANBUL]
        )
        locations[City.ST_PETERSBURG].add_connections(
            locations[City.ESSEN], locations[City.ISTANBUL], locations[City.MOSCOW]
        )
        locations[City.ALGIERS].add_connections(
            locations[City.MADRID], locations[City.PARIS], locations[City.ISTANBUL], locations[City.CAIRO]
        )
        locations[City.ISTANBUL].add_connections(
            locations[City.ALGIERS], locations[City.MILAN], locations[City.ST_PETERSBURG], locations[City.MOSCOW],
            locations[City.BAGHDAD]
        )
        locations[City.MOSCOW].add_connections(
            locations[City.ST_PETERSBURG], locations[City.ISTANBUL]
        )

        locations[City.BAGHDAD].add_connections(
            locations[City.ISTANBUL], locations[City.CAIRO], locations[City.RIYADH], locations[City.KARACHI]
        )
        locations[City.RIYADH].add_connections(
            locations[City.BAGHDAD], locations[City.CAIRO], locations[City.KARACHI]
        )
        locations[City.KARACHI].add_connections(
            locations[City.MUMBAI], locations[City.DELHI], locations[City.BAGHDAD], locations[City.RIYADH]
        )
        locations[City.MUMBAI].add_connections(
            locations[City.KARACHI], locations[City.DELHI], locations[City.CHENNAI]
        )
        locations[City.DELHI].add_connections(
            locations[City.KARACHI], locations[City.MUMBAI], locations[City.CHENNAI], locations[City.KOLKATA]
        )
        locations[City.CHENNAI].add_connections(
            locations[City.MUMBAI], locations[City.DELHI], locations[City.KOLKATA], locations[City.BANGKOK],
            locations[City.JAKARTA]
        )
        locations[City.KOLKATA].add_connections(
            locations[City.DELHI], locations[City.CHENNAI], locations[City.BANGKOK], locations[City.HONG_KONG]
        )
        locations[City.BANGKOK].add_connections(
            locations[City.KOLKATA], locations[City.CHENNAI], locations[City.HO_CHI_MINH_CITY], locations[City.HONG_KONG],
            locations[City.JAKARTA]
        )
        locations[City.HO_CHI_MINH_CITY].add_connections(
            locations[City.BANGKOK], locations[City.JAKARTA], locations[City.HONG_KONG], locations[City.MANILA]
        )
        locations[City.JAKARTA].add_connections(
            locations[City.SYDNEY], locations[City.MANILA], locations[City.HO_CHI_MINH_CITY], locations[City.BANGKOK]
        )

        locations[City.HONG_KONG].add_connections(
            locations[City.SHANGHAI], locations[City.TAIPEI], locations[City.MANILA], locations[City.HO_CHI_MINH_CITY],
            locations[City.BANGKOK], locations[City.SEOUL]
        )
        locations[City.SHANGHAI].add_connections(
            locations[City.BEIJING], locations[City.SEOUL], locations[City.TAIPEI], locations[City.HONG_KONG],
            locations[City.TOKYO]
        )
        locations[City.BEIJING].add_connections(
            locations[City.SHANGHAI], locations[City.SEOUL]
        )
        locations[City.SEOUL].add_connections(
            locations[City.BEIJING], locations[City.SHANGHAI], locations[City.TOKYO], locations[City.HONG_KONG]
        )
        locations[City.TAIPEI].add_connections(
            locations[City.SHANGHAI], locations[City.HONG_KONG], locations[City.OSAKA], locations[City.MANILA]
        )
        locations[City.OSAKA].add_connections(
            locations[City.TOKYO], locations[City.TAIPEI]
        )

        locations[City.SYDNEY].add_connections(
            locations[City.JAKARTA], locations[City.MANILA], locations[City.LOS_ANGELES]
        )

        locations[City.BOGOTA].add_connections(
            locations[City.MEXICO_CITY], locations[City.LIMA], locations[City.MIAMI], locations[City.SAO_PAULO],
            locations[City.BUENOS_AIRES]
        )
        locations[City.LIMA].add_connections(
            locations[City.MEXICO_CITY], locations[City.BOGOTA], locations[City.SANTIAGO]
        )
        locations[City.SANTIAGO].add_connections(
            locations[City.LIMA]
        )
        locations[City.SAO_PAULO].add_connections(
            locations[City.BOGOTA], locations[City.BUENOS_AIRES], locations[City.LAGOS], locations[City.MADRID]
        )
        locations[City.BUENOS_AIRES].add_connections(
            locations[City.BOGOTA], locations[City.SAO_PAULO]
        )

        locations[City.LAGOS].add_connections(
            locations[City.KINSHASA], locations[City.KHARTOUM], locations[City.SAO_PAULO]
        )
        locations[City.KINSHASA].add_connections(
            locations[City.LAGOS], locations[City.KHARTOUM], locations[City.JOHANNESBURG]
        )
        locations[City.KHARTOUM].add_connections(
            locations[City.CAIRO], locations[City.LAGOS], locations[City.KINSHASA], locations[City.JOHANNESBURG]
        )
        locations[City.JOHANNESBURG].add_connections(
            locations[City.KINSHASA], locations[City.KHARTOUM]
        )
        locations[City.CAIRO].add_connections(
            locations[City.ALGIERS], locations[City.ISTANBUL], locations[City.BAGHDAD], locations[City.RIYADH],
            locations[City.KHARTOUM]
        )
        return locations