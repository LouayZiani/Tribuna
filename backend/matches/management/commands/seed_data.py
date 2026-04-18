"""
seed_data.py — Full 2026 KPL Season
16 teams, 30 matchdays, ~240 fixtures (Mar–Nov 2026)
Run: python manage.py seed_data
Re-seed: python manage.py seed_data --force
"""
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from datetime import datetime
from matches.models import Match
from seats.models import Seat

TEAMS = {
    'FC Astana':         ('Astana Arena',                    'Astana',        15000, 5000),
    'Kairat Almaty':     ('Central Stadium',                 'Almaty',        14000, 4500),
    'Tobol Kostanay':    ('Tobol Stadium',                   'Kostanay',      10000, 3000),
    'Ordabasy':          ('Kazhimukan Munaitpasov Stadium',  'Shymkent',      11000, 3500),
    'Kyzylzhar':         ('Tsentralny Stadium',              'Petropavlovsk',  9000, 2800),
    'Aktobe':            ('Aktobe Central Stadium',          'Aktobe',        10000, 3000),
    'Atyrau':            ('Munayshi Stadium',                'Atyrau',        10000, 3000),
    'Kaisar Kyzylorda':  ('Kaisar Stadium',                  'Kyzylorda',      9000, 2500),
    'Okzhetpes':         ('Okzhetpes Stadium',               'Kokshetau',      8000, 2500),
    'Irtysh Pavlodar':   ('Irtysh Stadium',                  'Pavlodar',       9000, 2800),
    'Ulytau':            ('Ulytau Stadium',                  'Zhezkazgan',     8000, 2500),
    'Caspiy':            ('Caspiy Arena',                    'Aktau',          8000, 2500),
    'Jenys':             ('Jenys Stadium',                   'Astana',         9000, 2800),
    'Elimai':            ('Elimai Stadium',                  'Semey',          8000, 2500),
    'Altai':             ('Altai Stadium',                   'Oskemen',        8000, 2500),
    'Zhetysu':           ('Zhetysu Stadium',                 'Taldykorgan',    9000, 2800),
}

FIXTURES = [
    # MD1 Mar 7-8
    ('FC Astana','Kairat Almaty','2026-03-07 15:00'),('Tobol Kostanay','Ordabasy','2026-03-07 13:00'),
    ('Aktobe','Kyzylzhar','2026-03-07 14:00'),('Atyrau','Kaisar Kyzylorda','2026-03-07 14:00'),
    ('Irtysh Pavlodar','Okzhetpes','2026-03-07 13:00'),('Ulytau','Altai','2026-03-08 13:00'),
    ('Caspiy','Jenys','2026-03-08 14:00'),('Elimai','Zhetysu','2026-03-08 13:00'),
    # MD2 Mar 14-15
    ('Kairat Almaty','Tobol Kostanay','2026-03-14 15:00'),('Ordabasy','FC Astana','2026-03-14 13:00'),
    ('Kyzylzhar','Atyrau','2026-03-14 14:00'),('Kaisar Kyzylorda','Irtysh Pavlodar','2026-03-14 14:00'),
    ('Okzhetpes','Ulytau','2026-03-15 13:00'),('Altai','Caspiy','2026-03-15 14:00'),
    ('Jenys','Elimai','2026-03-15 13:00'),('Zhetysu','Aktobe','2026-03-15 14:00'),
    # MD3 Mar 21-22
    ('FC Astana','Ulytau','2026-03-21 15:00'),('Kairat Almaty','Ordabasy','2026-03-21 15:00'),
    ('Tobol Kostanay','Kyzylzhar','2026-03-21 13:00'),('Aktobe','Kaisar Kyzylorda','2026-03-21 14:00'),
    ('Atyrau','Okzhetpes','2026-03-21 14:00'),('Irtysh Pavlodar','Altai','2026-03-22 13:00'),
    ('Caspiy','Elimai','2026-03-22 14:00'),('Jenys','Zhetysu','2026-03-22 13:00'),
    # MD4 Mar 28-29
    ('Ordabasy','Tobol Kostanay','2026-03-28 13:00'),('Kyzylzhar','Kairat Almaty','2026-03-28 14:00'),
    ('Ulytau','Jenys','2026-03-28 13:00'),('Kaisar Kyzylorda','FC Astana','2026-03-28 14:00'),
    ('Okzhetpes','Caspiy','2026-03-29 13:00'),('Altai','Zhetysu','2026-03-29 14:00'),
    ('Elimai','Atyrau','2026-03-29 13:00'),('Zhetysu','Irtysh Pavlodar','2026-03-29 14:00'),
    # MD5 Apr 4-5
    ('FC Astana','Aktobe','2026-04-04 15:00'),('Kairat Almaty','Atyrau','2026-04-04 15:00'),
    ('Tobol Kostanay','Caspiy','2026-04-04 13:00'),('Ordabasy','Kyzylzhar','2026-04-04 13:00'),
    ('Irtysh Pavlodar','Jenys','2026-04-05 13:00'),('Ulytau','Kaisar Kyzylorda','2026-04-05 13:00'),
    ('Okzhetpes','Zhetysu','2026-04-05 14:00'),('Altai','Elimai','2026-04-05 14:00'),
    # MD6 Apr 11-12
    ('FC Astana','Ordabasy','2026-04-11 15:00'),('Tobol Kostanay','Kairat Almaty','2026-04-11 13:00'),
    ('Atyrau','Kaisar Kyzylorda','2026-04-11 14:00'),('Elimai','FC Astana','2026-04-11 13:00'),
    ('Irtysh Pavlodar','Zhetysu','2026-04-12 13:00'),('Aktobe','Caspiy','2026-04-12 14:00'),
    ('Kyzylzhar','Jenys','2026-04-12 14:00'),('Altai','Ulytau','2026-04-12 13:00'),
    # MD7 Apr 18-19
    ('Caspiy','Kairat Almaty','2026-04-18 13:00'),('Ordabasy','Okzhetpes','2026-04-18 14:00'),
    ('Ulytau','Tobol Kostanay','2026-04-19 10:00'),('Atyrau','Kyzylzhar','2026-04-19 11:00'),
    ('Jenys','Aktobe','2026-04-19 12:00'),('Kaisar Kyzylorda','Altai','2026-04-19 14:00'),
    ('FC Astana','Irtysh Pavlodar','2026-04-19 15:00'),('Zhetysu','Elimai','2026-04-19 13:00'),
    # MD8 Apr 25-26
    ('Okzhetpes','Kaisar Kyzylorda','2026-04-25 10:00'),('Altai','Jenys','2026-04-25 11:00'),
    ('Kyzylzhar','Ordabasy','2026-04-25 12:00'),('Aktobe','Irtysh Pavlodar','2026-04-25 14:00'),
    ('Kairat Almaty','Elimai','2026-04-26 15:00'),('Tobol Kostanay','Atyrau','2026-04-26 13:00'),
    ('Caspiy','Ulytau','2026-04-26 14:00'),('FC Astana','Zhetysu','2026-04-26 15:00'),
    # MD9 May 2-3
    ('FC Astana','Tobol Kostanay','2026-05-02 15:00'),('Kairat Almaty','Aktobe','2026-05-02 15:00'),
    ('Irtysh Pavlodar','Kyzylzhar','2026-05-02 13:00'),('Ordabasy','Atyrau','2026-05-02 13:00'),
    ('Jenys','Ulytau','2026-05-03 12:00'),('Elimai','Okzhetpes','2026-05-03 13:00'),
    ('Zhetysu','Caspiy','2026-05-03 14:00'),('Kaisar Kyzylorda','Altai','2026-05-03 14:00'),
    # MD10 May 9-10
    ('Aktobe','Ordabasy','2026-05-09 14:00'),('Kyzylzhar','FC Astana','2026-05-09 14:00'),
    ('Atyrau','Jenys','2026-05-09 14:00'),('Ulytau','Irtysh Pavlodar','2026-05-09 13:00'),
    ('Altai','Kairat Almaty','2026-05-10 14:00'),('Okzhetpes','Tobol Kostanay','2026-05-10 13:00'),
    ('Caspiy','Kaisar Kyzylorda','2026-05-10 14:00'),('Elimai','Zhetysu','2026-05-10 13:00'),
    # MD11 May 16-17
    ('FC Astana','Jenys','2026-05-16 15:00'),('Kairat Almaty','Irtysh Pavlodar','2026-05-16 15:00'),
    ('Tobol Kostanay','Altai','2026-05-16 13:00'),('Ordabasy','Caspiy','2026-05-16 13:00'),
    ('Kaisar Kyzylorda','Elimai','2026-05-17 14:00'),('Kyzylzhar','Ulytau','2026-05-17 14:00'),
    ('Aktobe','Zhetysu','2026-05-17 14:00'),('Atyrau','Okzhetpes','2026-05-17 14:00'),
    # MD12 May 23-24
    ('Irtysh Pavlodar','FC Astana','2026-05-23 13:00'),('Jenys','Kairat Almaty','2026-05-23 13:00'),
    ('Ulytau','Ordabasy','2026-05-23 13:00'),('Altai','Aktobe','2026-05-24 14:00'),
    ('Caspiy','Atyrau','2026-05-24 14:00'),('Elimai','Tobol Kostanay','2026-05-24 13:00'),
    ('Zhetysu','Kaisar Kyzylorda','2026-05-24 14:00'),('Okzhetpes','Kyzylzhar','2026-05-24 13:00'),
    # MD13 May 30-31
    ('FC Astana','Altai','2026-05-30 15:00'),('Kairat Almaty','Caspiy','2026-05-30 15:00'),
    ('Tobol Kostanay','Ulytau','2026-05-30 13:00'),('Ordabasy','Elimai','2026-05-30 13:00'),
    ('Aktobe','Okzhetpes','2026-05-31 14:00'),('Atyrau','Irtysh Pavlodar','2026-05-31 14:00'),
    ('Kyzylzhar','Zhetysu','2026-05-31 14:00'),('Kaisar Kyzylorda','Jenys','2026-05-31 13:00'),
    # MD14 Jun 6-7
    ('Caspiy','Ordabasy','2026-06-06 14:00'),('Elimai','Aktobe','2026-06-06 13:00'),
    ('Ulytau','Kairat Almaty','2026-06-06 13:00'),('Altai','Tobol Kostanay','2026-06-06 14:00'),
    ('Irtysh Pavlodar','Kaisar Kyzylorda','2026-06-07 13:00'),('Jenys','FC Astana','2026-06-07 13:00'),
    ('Zhetysu','Atyrau','2026-06-07 14:00'),('Okzhetpes','Elimai','2026-06-07 13:00'),
    # MD15 Jun 20-21
    ('FC Astana','Kyzylzhar','2026-06-20 15:00'),('Kairat Almaty','Zhetysu','2026-06-20 15:00'),
    ('Tobol Kostanay','Kaisar Kyzylorda','2026-06-20 13:00'),('Ordabasy','Irtysh Pavlodar','2026-06-20 13:00'),
    ('Aktobe','Ulytau','2026-06-21 14:00'),('Atyrau','Altai','2026-06-21 14:00'),
    ('Caspiy','FC Astana','2026-06-21 14:00'),('Jenys','Okzhetpes','2026-06-21 13:00'),
    # MD16 Jun 27-28
    ('Kaisar Kyzylorda','Kairat Almaty','2026-06-27 14:00'),('Kyzylzhar','Tobol Kostanay','2026-06-27 14:00'),
    ('Irtysh Pavlodar','Aktobe','2026-06-27 13:00'),('Ulytau','FC Astana','2026-06-27 13:00'),
    ('Altai','Ordabasy','2026-06-28 14:00'),('Zhetysu','Jenys','2026-06-28 14:00'),
    ('Elimai','Caspiy','2026-06-28 13:00'),('Okzhetpes','Atyrau','2026-06-28 13:00'),
    # MD17 Jul 4-5
    ('FC Astana','Ordabasy','2026-07-04 19:00'),('Kairat Almaty','Tobol Kostanay','2026-07-04 19:00'),
    ('Aktobe','Atyrau','2026-07-04 17:00'),('Caspiy','Kyzylzhar','2026-07-04 17:00'),
    ('Jenys','Irtysh Pavlodar','2026-07-05 17:00'),('Okzhetpes','Altai','2026-07-05 17:00'),
    ('Zhetysu','Ulytau','2026-07-05 17:00'),('Kaisar Kyzylorda','Elimai','2026-07-05 17:00'),
    # MD18 Jul 11-12
    ('Tobol Kostanay','FC Astana','2026-07-11 17:00'),('Ordabasy','Kairat Almaty','2026-07-11 17:00'),
    ('Atyrau','Aktobe','2026-07-11 17:00'),('Kyzylzhar','Caspiy','2026-07-11 17:00'),
    ('Irtysh Pavlodar','Jenys','2026-07-12 17:00'),('Altai','Okzhetpes','2026-07-12 17:00'),
    ('Ulytau','Zhetysu','2026-07-12 17:00'),('Elimai','Kaisar Kyzylorda','2026-07-12 17:00'),
    # MD19 Jul 18-19
    ('FC Astana','Caspiy','2026-07-18 19:00'),('Kairat Almaty','Kyzylzhar','2026-07-18 19:00'),
    ('Tobol Kostanay','Irtysh Pavlodar','2026-07-18 17:00'),('Ordabasy','Jenys','2026-07-18 17:00'),
    ('Aktobe','Altai','2026-07-19 17:00'),('Atyrau','Elimai','2026-07-19 17:00'),
    ('Okzhetpes','Ulytau','2026-07-19 17:00'),('Kaisar Kyzylorda','Zhetysu','2026-07-19 17:00'),
    # MD20 Jul 25-26
    ('Caspiy','Tobol Kostanay','2026-07-25 17:00'),('Jenys','Kairat Almaty','2026-07-25 17:00'),
    ('Kyzylzhar','Ordabasy','2026-07-25 17:00'),('Irtysh Pavlodar','Atyrau','2026-07-25 17:00'),
    ('Altai','FC Astana','2026-07-26 17:00'),('Ulytau','Aktobe','2026-07-26 17:00'),
    ('Zhetysu','Okzhetpes','2026-07-26 17:00'),('Elimai','Jenys','2026-07-26 17:00'),
    # MD21 Aug 1-2
    ('FC Astana','Tobol Kostanay','2026-08-01 19:00'),('Kairat Almaty','Atyrau','2026-08-01 19:00'),
    ('Ordabasy','Altai','2026-08-01 17:00'),('Aktobe','Caspiy','2026-08-01 17:00'),
    ('Kaisar Kyzylorda','Kyzylzhar','2026-08-02 17:00'),('Irtysh Pavlodar','Zhetysu','2026-08-02 17:00'),
    ('Okzhetpes','Jenys','2026-08-02 17:00'),('Ulytau','Elimai','2026-08-02 17:00'),
    # MD22 Aug 8-9
    ('Tobol Kostanay','Ordabasy','2026-08-08 17:00'),('Atyrau','FC Astana','2026-08-08 17:00'),
    ('Altai','Kairat Almaty','2026-08-08 17:00'),('Caspiy','Aktobe','2026-08-08 17:00'),
    ('Kyzylzhar','Kaisar Kyzylorda','2026-08-09 17:00'),('Zhetysu','Irtysh Pavlodar','2026-08-09 17:00'),
    ('Jenys','Okzhetpes','2026-08-09 17:00'),('Elimai','Ulytau','2026-08-09 17:00'),
    # MD23 Aug 15-16
    ('FC Astana','Kaisar Kyzylorda','2026-08-15 19:00'),('Kairat Almaty','Okzhetpes','2026-08-15 19:00'),
    ('Tobol Kostanay','Zhetysu','2026-08-15 17:00'),('Ordabasy','Ulytau','2026-08-15 17:00'),
    ('Aktobe','Jenys','2026-08-16 17:00'),('Atyrau','Caspiy','2026-08-16 17:00'),
    ('Irtysh Pavlodar','Altai','2026-08-16 17:00'),('Kyzylzhar','Elimai','2026-08-16 17:00'),
    # MD24 Aug 22-23
    ('Kaisar Kyzylorda','Tobol Kostanay','2026-08-22 17:00'),('Okzhetpes','Aktobe','2026-08-22 17:00'),
    ('Ulytau','Kyzylzhar','2026-08-22 17:00'),('Caspiy','Irtysh Pavlodar','2026-08-22 17:00'),
    ('Altai','Atyrau','2026-08-23 17:00'),('Jenys','Ordabasy','2026-08-23 17:00'),
    ('Zhetysu','FC Astana','2026-08-23 17:00'),('Elimai','Kairat Almaty','2026-08-23 17:00'),
    # MD25 Sep 12-13
    ('FC Astana','Okzhetpes','2026-09-12 16:00'),('Kairat Almaty','Kaisar Kyzylorda','2026-09-12 16:00'),
    ('Tobol Kostanay','Jenys','2026-09-12 14:00'),('Ordabasy','Zhetysu','2026-09-12 14:00'),
    ('Aktobe','Elimai','2026-09-13 14:00'),('Atyrau','Ulytau','2026-09-13 14:00'),
    ('Irtysh Pavlodar','Caspiy','2026-09-13 14:00'),('Kyzylzhar','Altai','2026-09-13 14:00'),
    # MD26 Sep 19-20
    ('Okzhetpes','FC Astana','2026-09-19 14:00'),('Kaisar Kyzylorda','Ordabasy','2026-09-19 14:00'),
    ('Jenys','Tobol Kostanay','2026-09-19 14:00'),('Zhetysu','Aktobe','2026-09-19 14:00'),
    ('Ulytau','Atyrau','2026-09-20 14:00'),('Caspiy','Kyzylzhar','2026-09-20 14:00'),
    ('Altai','Irtysh Pavlodar','2026-09-20 14:00'),('Elimai','Kairat Almaty','2026-09-20 14:00'),
    # MD27 Sep 26-27
    ('FC Astana','Elimai','2026-09-26 16:00'),('Kairat Almaty','Ulytau','2026-09-26 16:00'),
    ('Tobol Kostanay','Okzhetpes','2026-09-26 14:00'),('Ordabasy','Kaisar Kyzylorda','2026-09-26 14:00'),
    ('Aktobe','Atyrau','2026-09-27 14:00'),('Irtysh Pavlodar','FC Astana','2026-09-27 14:00'),
    ('Kyzylzhar','Jenys','2026-09-27 14:00'),('Altai','Zhetysu','2026-09-27 14:00'),
    # MD28 Oct 3-4
    ('FC Astana','Aktobe','2026-10-03 16:00'),('Kairat Almaty','Jenys','2026-10-03 16:00'),
    ('Ordabasy','Tobol Kostanay','2026-10-03 14:00'),('Atyrau','Irtysh Pavlodar','2026-10-03 14:00'),
    ('Kaisar Kyzylorda','Caspiy','2026-10-04 14:00'),('Ulytau','Altai','2026-10-04 14:00'),
    ('Zhetysu','Kyzylzhar','2026-10-04 14:00'),('Elimai','Okzhetpes','2026-10-04 14:00'),
    # MD29 Oct 17-18
    ('Tobol Kostanay','Aktobe','2026-10-17 14:00'),('Kyzylzhar','Irtysh Pavlodar','2026-10-17 14:00'),
    ('Jenys','Atyrau','2026-10-17 14:00'),('Caspiy','Zhetysu','2026-10-17 14:00'),
    ('Altai','Kaisar Kyzylorda','2026-10-18 14:00'),('Okzhetpes','Ordabasy','2026-10-18 13:00'),
    ('Ulytau','FC Astana','2026-10-18 13:00'),('Elimai','Tobol Kostanay','2026-10-18 14:00'),
    # MD30 — Final Day Nov 1
    ('FC Astana','Kairat Almaty','2026-11-01 16:00'),('Tobol Kostanay','Atyrau','2026-11-01 14:00'),
    ('Ordabasy','Aktobe','2026-11-01 14:00'),('Kyzylzhar','Okzhetpes','2026-11-01 14:00'),
    ('Kaisar Kyzylorda','Ulytau','2026-11-01 14:00'),('Irtysh Pavlodar','Elimai','2026-11-01 14:00'),
    ('Jenys','Caspiy','2026-11-01 14:00'),('Zhetysu','Altai','2026-11-01 14:00'),
]

VIP_ROWS      = ['A', 'B']
REGULAR_ROWS  = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
SEATS_PER_ROW = 20


class Command(BaseCommand):
    help = 'Seed database with full 2026 KPL season (16 teams, 30 matchdays, ~240 fixtures)'

    def add_arguments(self, parser):
        parser.add_argument('--force', action='store_true', help='Clear and re-seed')

    def handle(self, *args, **kwargs):
        if Match.objects.exists() and not kwargs.get('force'):
            self.stdout.write(self.style.WARNING('Already seeded. Use --force to re-seed.'))
            return
        if kwargs.get('force'):
            self.stdout.write('Clearing existing data...')
            Seat.objects.all().delete()
            Match.objects.all().delete()

        total = (len(VIP_ROWS) + len(REGULAR_ROWS)) * SEATS_PER_ROW
        mc = 0

        self.stdout.write(f'\nSeeding {len(FIXTURES)} KPL 2026 fixtures...\n')

        for home, away, dt_str in FIXTURES:
            if home not in TEAMS or away not in TEAMS:
                self.stdout.write(self.style.WARNING(f'  Unknown team: {home} vs {away}'))
                continue

            stadium, city, vip_p, reg_p = TEAMS[home]
            dt = make_aware(datetime.strptime(dt_str, '%Y-%m-%d %H:%M'))

            match = Match.objects.create(
                home_team=home, away_team=away, date=dt,
                stadium=stadium, city=city,
                total_seats=total, available_seats=total,
                vip_price=vip_p, regular_price=reg_p,
            )

            seats = []
            for row in VIP_ROWS:
                for n in range(1, SEATS_PER_ROW + 1):
                    seats.append(Seat(match=match, row=row, number=n, section='VIP'))
            for row in REGULAR_ROWS:
                for n in range(1, SEATS_PER_ROW + 1):
                    seats.append(Seat(match=match, row=row, number=n, section='Regular'))
            Seat.objects.bulk_create(seats)
            mc += 1
            self.stdout.write(f'  + {home} vs {away}  [{dt_str}]')

        self.stdout.write(self.style.SUCCESS(
            f'\nDone! {mc} matches, {mc * total:,} seats total.'
        ))
