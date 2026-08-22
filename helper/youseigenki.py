# Notes: TODO: simultaneous with using the circle list pages
import sys
import json
from pathlib import Path
from typing import Any

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

RT, OT = ReliabilityTypes, OriginTypes

PATH_HELPER = Path(__file__).parent
PATH_EVENT_GROUP = PATH_HELPER.parent
PATH_MEDIA = PATH_EVENT_GROUP / "media"


def retrieve_circles(event_name: str) -> list[Circle]:
    """Retrieve circles of given event. In the circle file has not been created, execute the creation script first."""
    circles_json_path = PATH_HELPER / event_name / "circles.json"
    if not circles_json_path.exists():
        print(
            f"Circle file for {event_name} not found, running the creation script ..."
        )
        creation_script_path = PATH_HELPER / event_name / "main.py"
        if not creation_script_path.exists():
            raise FileNotFoundError(
                f"Creation script for {event_name} not found at {creation_script_path}"
            )
        # Import main() from the creation script and execute
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            f"{event_name}.main", creation_script_path
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "main"):
                module.main()

        if not circles_json_path.exists():
            raise FileNotFoundError(
                f"Creation script {creation_script_path} failed to create {circles_json_path}"
            )

    with circles_json_path.open("r", encoding="utf-8") as f:
        circles_raw = json.load(f)
    return [Circle.load_from_json(c) for c in circles_raw]


if __name__ == "__main__":
    events: list[Event] = []
    active_events: list[int | str] = list(range(1, 18 + 1))

    thwikicc = "https://thwiki.cc/%E5%A6%96%E7%B2%BE%E5%85%83%E6%B0%94%EF%BC%81"

    i = 1  # ==== youseigenki1 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "01_cirno_top2.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20101231035441/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by HAM（points)",
            ),
            Medium(
                "01_539px-妖精元气！1插画.jpg",
                [Source(thwikicc, (ReliabilityTypes.Reliable, OriginTypes.Official))],
            ),
        ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1 Chome-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザＰＩＯ大展示",
                sources=[
                    Source(
                        "https://web.archive.org/web/20100222144933/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlSopXAxX4zYII19vbdI4rX0w5RiVyPdD_3T-rcKAI3NBfzD7cKS2HEXWrr_JXATLT3BXULla2lC3oHidDik9oIlyt_6fS4t9y2wbW_lLHAvuil4Cw0WsOtevHY2sumWk6a1Mp8Hg=s0?imgmax=0",
                url="https://maps.app.goo.gl/mSxwaUchFHGpFwBf9",
            ),
        ]
        event = Event(
            aliases=[
                "ようせいげんき！",
                "Yousei Genki!",
                f"ようせいげんき！{i}",
                f"Yousei Genki! {i}",
            ],
            dates="2010.09.05",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20100222144933/http://www.puniket.com/cirno/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20110811213205/http://www.puniket.com/cirno/cirno_list01.htm",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="Simultanous with 幺樂団カァニバル！.",
            comments=None,
            last_edited="2026.08.21",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 2  # ==== youseigenki2 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
            # Medium("", [Source("", (RT.Reliable, OT.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.655153, 139.7607689),
                address="Japan, 〒105-7501 Tokyo, Minato City, Kaigan, 1 Chome−7−1 東京ポートシティ竹芝オフィスタワ",
                comments=None,
                description="都立産業貿易センター浜松町館 ４、５Ｆ（２フロア開催予定）",
                sources=[
                    Source(
                        "https://web.archive.org/web/20120118101603/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmihIGbPitN7h8Vc_sXo8I679FTgrlkYst2LWaAy_Wl45MDqMaFnozSO4Y2Vud8h07FgRpXdq_CPW3IWnFwj-AyKuJ0L7ShZyQ41TQcBAFNOouYZR3jFZXxn_SQsgsK-FST-5JK8g=w408-h544-k-no",
                url="https://maps.app.goo.gl/ZF8XaGQinUTwnNMw6",
            ),
        ]
        event = Event(
            aliases=[
                f"ようせいげんき！{i}",
                f"Yousei Genki! {i}",
            ],
            dates="2011.09.19",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20120118101603/http://www.puniket.com/cirno/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.21",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 3  # ==== youseigenki3 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "03_531px-妖精元气！3.jpg",
                [Source(thwikicc, (ReliabilityTypes.Reliable, OriginTypes.Official))],
                comments="Illustration by HAM（points)",
            ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.655153, 139.7607689),
                address="Japan, 〒105-7501 Tokyo, Minato City, Kaigan, 1 Chome−7−1 東京ポートシティ竹芝オフィスタワ",
                comments=None,
                description="都立産業貿易センター浜松町館",
                sources=[
                    Source(
                        "https://web.archive.org/web/20120118101603/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWmihIGbPitN7h8Vc_sXo8I679FTgrlkYst2LWaAy_Wl45MDqMaFnozSO4Y2Vud8h07FgRpXdq_CPW3IWnFwj-AyKuJ0L7ShZyQ41TQcBAFNOouYZR3jFZXxn_SQsgsK-FST-5JK8g=w408-h544-k-no",
                url="https://maps.app.goo.gl/ZF8XaGQinUTwnNMw6",
            ),
        ]
        event = Event(
            aliases=[
                f"ようせいげんき！{i}",
                f"Yousei Genki! {i}",
            ],
            dates="2012.09.09",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20121016051727/http://www.puniket.com/cirno/",
                    (RT.Reliable, OT.Official),
                ),
                # Source("Participating circles: ", (RT.Reliable, OT.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.21",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 4  # ==== youseigenki4 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "04_cirno_top4_01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20130119161557/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by HAM（points)",
            ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1 Chome-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザＰｉＯ大展示ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20130119161557/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlSopXAxX4zYII19vbdI4rX0w5RiVyPdD_3T-rcKAI3NBfzD7cKS2HEXWrr_JXATLT3BXULla2lC3oHidDik9oIlyt_6fS4t9y2wbW_lLHAvuil4Cw0WsOtevHY2sumWk6a1Mp8Hg=s0?imgmax=0",
                url="https://maps.app.goo.gl/mSxwaUchFHGpFwBf9",
            ),
        ]
        event = Event(
            aliases=[
                f"ようせいげんき！{i}",
                f"Yousei Genki! {i}",
            ],
            dates="2013.01.27",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20130119161557/http://www.puniket.com/cirno/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20130323154552/http://www.puniket.com/aka/2013_0127_lisi02.htm",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.21",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 5  # ==== youseigenki5 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "05_cirno_top5_01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20130812023818/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by HAM（points)",
            ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1 Chome-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザＰｉＯ大展示ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20130812023818/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlSopXAxX4zYII19vbdI4rX0w5RiVyPdD_3T-rcKAI3NBfzD7cKS2HEXWrr_JXATLT3BXULla2lC3oHidDik9oIlyt_6fS4t9y2wbW_lLHAvuil4Cw0WsOtevHY2sumWk6a1Mp8Hg=s0?imgmax=0",
                url="https://maps.app.goo.gl/mSxwaUchFHGpFwBf9",
            ),
        ]
        event = Event(
            aliases=[
                f"ようせいげんき！{i}",
                f"Yousei Genki! {i}",
            ],
            dates="2013.09.08",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20130812023818/http://www.puniket.com/cirno/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                # Source("Participating circles: ", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.22",
        )

        # Retrieve circles
        # event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 6  # ==== youseigenki6 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "06_cirno_top6_01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20141105010647/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by HAM（points)",
            ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1 Chome-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザＰｉＯ大展示ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20141105010647/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlSopXAxX4zYII19vbdI4rX0w5RiVyPdD_3T-rcKAI3NBfzD7cKS2HEXWrr_JXATLT3BXULla2lC3oHidDik9oIlyt_6fS4t9y2wbW_lLHAvuil4Cw0WsOtevHY2sumWk6a1Mp8Hg=s0?imgmax=0",
                url="https://maps.app.goo.gl/mSxwaUchFHGpFwBf9",
            ),
        ]
        event = Event(
            aliases=[
                f"ようせいげんき！{i}",
                f"Yousei Genki! {i}",
            ],
            dates="2014.01.12",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20141105010647/http://www.puniket.com/cirno/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20131229062508/http://www.puniket.com/aka/0112toho_aka11_list02.htm",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.22",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 7  # ==== youseigenki7 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "07_cirno_top7_01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20150622183222/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by HAM（points)",
            ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1 Chome-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザＰｉＯ大展示ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20150622183222/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlSopXAxX4zYII19vbdI4rX0w5RiVyPdD_3T-rcKAI3NBfzD7cKS2HEXWrr_JXATLT3BXULla2lC3oHidDik9oIlyt_6fS4t9y2wbW_lLHAvuil4Cw0WsOtevHY2sumWk6a1Mp8Hg=s0?imgmax=0",
                url="https://maps.app.goo.gl/mSxwaUchFHGpFwBf9",
            ),
        ]
        event = Event(
            aliases=[
                f"ようせいげんき！{i}",
                f"Yousei Genki! {i}",
            ],
            dates="2015.03.14",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20150622183222/http://www.puniket.com/cirno/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20150313173421/http://www.puniket.com/aka/aka12_list02.htm",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.22",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 8  # ==== youseigenki8 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "08_cirno_top8_01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20160704031420/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by HAM（points)",
            ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1 Chome-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザＰＩＯ １Ｆ大展示ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20160704031420/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlSopXAxX4zYII19vbdI4rX0w5RiVyPdD_3T-rcKAI3NBfzD7cKS2HEXWrr_JXATLT3BXULla2lC3oHidDik9oIlyt_6fS4t9y2wbW_lLHAvuil4Cw0WsOtevHY2sumWk6a1Mp8Hg=s0?imgmax=0",
                url="https://maps.app.goo.gl/mSxwaUchFHGpFwBf9",
            ),
        ]
        event = Event(
            aliases=[
                f"ようせいげんき！{i}",
                f"Yousei Genki! {i}",
            ],
            dates="2016.01.24",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20160704031420/http://www.puniket.com/cirno/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20160113213041/http://www.puniket.com/aka/touhou124_list02.htm",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.22",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 9  # ==== youseigenki9 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "09_cirno_top9_01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20170822143330/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by HAM（points)",
            ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1 Chome-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザＰＩＯ １Ｆ大展示ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20170822143330/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlSopXAxX4zYII19vbdI4rX0w5RiVyPdD_3T-rcKAI3NBfzD7cKS2HEXWrr_JXATLT3BXULla2lC3oHidDik9oIlyt_6fS4t9y2wbW_lLHAvuil4Cw0WsOtevHY2sumWk6a1Mp8Hg=s0?imgmax=0",
                url="https://maps.app.goo.gl/mSxwaUchFHGpFwBf9",
            ),
        ]
        event = Event(
            aliases=[
                f"ようせいげんき！{i}",
                f"Yousei Genki! {i}",
            ],
            dates="2017.01.29",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20170822143330/http://www.puniket.com/cirno/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20170202002107/http://www.puniket.com/aka/aka14_list02.htm",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.22",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 10  # ==== youseigenki10 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "10_cirno_top10_01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20180524070705/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by HAM（points)",
            ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1 Chome-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザＰＩＯ １Ｆ大展示ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20180524070705/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlSopXAxX4zYII19vbdI4rX0w5RiVyPdD_3T-rcKAI3NBfzD7cKS2HEXWrr_JXATLT3BXULla2lC3oHidDik9oIlyt_6fS4t9y2wbW_lLHAvuil4Cw0WsOtevHY2sumWk6a1Mp8Hg=s0?imgmax=0",
                url="https://maps.app.goo.gl/mSxwaUchFHGpFwBf9",
            ),
        ]
        event = Event(
            aliases=[
                f"ようせいげんき！{i}",
                f"Yousei Genki! {i}",
            ],
            dates="2018.02.11",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20180524070705/http://www.puniket.com/cirno/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20180212143447/http://www.puniket.com/aka/toho2018haru_list02.htm",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.22",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 11  # ==== youseigenki11 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium("11_cirno_top11_01.jpg",
                   [Source("https://web.archive.org/web/20181017031647/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1 Chome-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザＰＩＯ １Ｆ大展示ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20180524070705/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlSopXAxX4zYII19vbdI4rX0w5RiVyPdD_3T-rcKAI3NBfzD7cKS2HEXWrr_JXATLT3BXULla2lC3oHidDik9oIlyt_6fS4t9y2wbW_lLHAvuil4Cw0WsOtevHY2sumWk6a1Mp8Hg=s0?imgmax=0",
                url="https://maps.app.goo.gl/mSxwaUchFHGpFwBf9",
            ),
        ]
        event = Event(
            aliases=[
                f"ようせいげんき！{i}",
                f"Yousei Genki! {i}",
            ],
            dates="2018.09.15",
            circles=[],
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20181017031647/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20211203033926/http://www.puniket.com/aka/toho2018aki_list02.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.22",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 12  # ==== youseigenki12 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium("12_cirno_top12_01.jpg",
                   [Source("https://web.archive.org/web/20190921115430/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official))],
                   comments="Illustration by HAM（points)"),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
            ]
        locations = [
            Location(
                coordinates=(35.5587817, 139.7240667),
                address="1 Chome-20-20 Minamikamata, Ota City, Tokyo 144-0035, Japan",
                description="大田区産業プラザＰＩＯ １Ｆ大展示ホール",
                sources=[
                    Source(
                        "https://web.archive.org/web/20190921115430/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.OfficialExt),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWlSopXAxX4zYII19vbdI4rX0w5RiVyPdD_3T-rcKAI3NBfzD7cKS2HEXWrr_JXATLT3BXULla2lC3oHidDik9oIlyt_6fS4t9y2wbW_lLHAvuil4Cw0WsOtevHY2sumWk6a1Mp8Hg=s0?imgmax=0",
                url="https://maps.app.goo.gl/mSxwaUchFHGpFwBf9",
            ),
        ]
        event = Event(
            aliases=[
                f"ようせいげんき！{i}",
                f"Yousei Genki! {i}",
            ],
            dates="2019.01.27",
            circles=[],
            media=media_,
            sources=[
                Source("Date: https://web.archive.org/web/20190921115430/http://www.puniket.com/cirno/", (ReliabilityTypes.Reliable, OriginTypes.Official)),
                Source("Participating circles: https://web.archive.org/web/20220828175049/http://www.puniket.com/aka/toho2019haru_list02.htm", (ReliabilityTypes.Reliable, OriginTypes.Official)),
            ],
            locations=locations,
            description=None,
            # comments=None,
            last_edited="2026.08.22",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    # i =   # ==== youseigenki ====
    # if i in active_events:
    #     event_name = f"youseigenki{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=[
    #             f"ようせいげんき！{i}",
    #             f"Yousei Genki! {i}",
    #         ],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source(f"Date: {}", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         last_edited="2026.08.22",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # i =   # ==== youseigenki ====
    # if i in active_events:
    #     event_name = f"youseigenki{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=[
    #             f"ようせいげんき！{i}",
    #             f"Yousei Genki! {i}",
    #         ],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source(f"Date: {}", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         last_edited="2026.08.22",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # i =   # ==== youseigenki ====
    # if i in active_events:
    #     event_name = f"youseigenki{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=[
    #             f"ようせいげんき！{i}",
    #             f"Yousei Genki! {i}",
    #         ],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source(f"Date: {}", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         last_edited="2026.08.22",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # i =   # ==== youseigenki ====
    # if i in active_events:
    #     event_name = f"youseigenki{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=[
    #             f"ようせいげんき！{i}",
    #             f"Yousei Genki! {i}",
    #         ],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source(f"Date: {}", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         last_edited="2026.08.22",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # i =   # ==== youseigenki ====
    # if i in active_events:
    #     event_name = f"youseigenki{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=[
    #             f"ようせいげんき！{i}",
    #             f"Yousei Genki! {i}",
    #         ],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source(f"Date: {}", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         last_edited="2026.08.22",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # i =   # ==== youseigenki ====
    # if i in active_events:
    #     event_name = f"youseigenki{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=[
    #             f"ようせいげんき！{i}",
    #             f"Yousei Genki! {i}",
    #         ],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source(f"Date: {}", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         last_edited="2026.08.22",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # i =   # ==== youseigenki ====
    # if i in active_events:
    #     event_name = f"youseigenki{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=[
    #             f"ようせいげんき！{i}",
    #             f"Yousei Genki! {i}",
    #         ],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source(f"Date: {}", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         last_edited="2026.08.22",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # i =   # ==== youseigenki ====
    # if i in active_events:
    #     event_name = f"youseigenki{i}"
    #     print(f"Processing {event_name} ...")

    #     media_ = [
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #         # Medium("", [Source("", (RT.Reliable, OT.Official))]),
    #     ]
    #     locations = [
    #         # Location(
    #         #     coordinates=(,),
    #         #     address="",
    #         #     description="",
    #         #     sources=[Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))],
    #         #     # comments=None,
    #         #     imageUrl="",
    #         #     url="",
    #         # ),
    #     ]
    #     event = Event(
    #         aliases=[
    #             f"ようせいげんき！{i}",
    #             f"Yousei Genki! {i}",
    #         ],
    #         dates="",
    #         circles=[],
    #         media=media_,
    #         sources=[
    #             # Source(f"Date: {}", (RT.Reliable, OT.Official)),
    #             # Source("Participating circles: ", (RT.Reliable, OT.Official)),
    #         ],
    #         locations=locations,
    #         description=None,
    #         # comments=None,
    #         last_edited="2026.08.22",
    #     )

    #     # Retrieve circles
    #     # event.circles = retrieve_circles(event_name)
    #     events.append(event)

    # ==== event group ====
    media = [
        Medium(
            "eg_cirno_ba01b.jpg",
            [
                Source(
                    "https://web.archive.org/web/20100710045110/http://www.puniket.com/cirno/ol_cirno.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                )
            ],
        ),
        Medium(
            "eg_cirno_cut1.png",
            [
                Source(
                    "https://web.archive.org/web/20100710045019/http://www.puniket.com/cirno/event.html",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                )
            ],
            comments="Illustration by いちご",
        ),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        # Medium("",
        #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
    ]
    links = ["https://web.archive.org/web/20100702061047/http://www.puniket.com/cirno/"]

    event_group = EventGroup(
        aliases=[
            "ようせいげんき！",
            "Yousei Genki!",
        ],
        events=events,
        media=media,
        links=links,
        sources=[
            # Source(
            #     "",
            #     (ReliabilityTypes.Reliable, OriginTypes.Official),
            # ),
        ],
        comments=None,
        description=None,
        last_edited="2026.08.20",
    )

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
