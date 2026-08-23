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
    active_events: list[int | str] = list(range(1, 19 + 1))

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
            description="At a venue featuring 紅のひろば８, このはな咲夜３ and ようせいげんき！３",
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
            description="At a venue featuring 紅のひろば９, このはな咲夜４, ようせいげんき！４ and 遊音ファンタジウム２」",
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
            description="At a venue featuring 紅のひろば１０, このはな咲夜５, ようせいげんき！５ and 遊音ファンタジウム",
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
            description="At a venue featuring 紅のひろば１１, このはな咲夜６ and ようせいげんき！６",
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
            description="At a venue featuring 紅のひろば１２, このはな咲夜７, ようせいげんき！７ and 旧地獄温泉 お燐の湯",
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
            description="At 東方合同イベント2016新春！, which featured 紅のひろば１３, このはな咲夜８, ようせいげんき！８, 恋のまほうは魔理沙におまかせ！７, 七色魔女の人形舞踏会。５＆七曜魔女の舞踏会。５, 旧地獄温泉 お燐の湯 and もりや神社例大祭 五",
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
            description="At 東方合同イベント2017新春！, which featured 紅のひろば１４, このはな咲夜９, ようせいげんき！９, 恋のまほうは魔理沙におまかせ！８, 七色魔女の人形舞踏会。６＆七曜魔女の舞踏会。６, 旧地獄温泉 お燐の湯, もりや神社例大祭 六, みょうれんパーティー３, ゆゆみょん!５, 八雲のヒミツ基地 and 萃香粋酔（すいかすいすい）",
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
            description="At 東方合同イベント2018春！, which featured 紅のひろば１５, このはな咲夜１０, ようせいげんき！１０, 恋のまほうは魔理沙におまかせ！９, 七色魔女の人形舞踏会。７＆七曜魔女の舞踏会。７, 旧地獄温泉 お燐の湯, もりや神社例大祭 七, みょうれんパーティー４, ゆゆみょん!６, 八雲のヒミツ基地２ and 萃香粋酔２（すいかすいすい）",
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
            Medium(
                "11_cirno_top11_01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20181017031647/http://www.puniket.com/cirno/",
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
            dates="2018.09.15",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20181017031647/http://www.puniket.com/cirno/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20211203033926/http://www.puniket.com/aka/toho2018aki_list02.htm",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="At 東方合同イベント2018秋！, which featured 紅のひろば１６, このはな咲夜１１, ようせいげんき！１１, 恋のまほうは魔理沙におまかせ！１０, 七色魔女の人形舞踏会。８＆七曜魔女の舞踏会。８, 八雲のヒミツ基地３ and 萃香粋酔３（すいかすいすい）",
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
            Medium(
                "12_cirno_top12_01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20190921115430/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by HAM（points)",
            ),
            Medium(
                "14_aka19_zumen.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20210120215638/http://www.puniket.com/aka/aka19_zumen.pdf",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
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
                Source(
                    "Date: https://web.archive.org/web/20190921115430/http://www.puniket.com/cirno/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20220828175049/http://www.puniket.com/aka/toho2019haru_list02.htm",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="At 東方合同イベント2019新春！, which featured  紅のひろば１７, このはな咲夜１２, ようせいげんき！１２, 恋のまほうは魔理沙におまかせ！１１, 七色魔女の人形舞踏会。９＆七曜魔女の舞踏会。９, 旧地獄温泉 お燐の湯, もりや神社例大祭 八, みょうれんパーティー５, ゆゆみょん!７, 八雲のヒミツ基地４ and 萃香粋酔４（すいかすいすい）",
            # comments=None,
            last_edited="2026.08.22",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 13  # ==== youseigenki13 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "13_cirno_top13_01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20200224140724/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by HAM（points)",
            ),
            Medium(
                "https://web.archive.org/web/20200928075406/http://www.puniket.com/aka/toho2020_0202w.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20200928075406/http://www.puniket.com/aka/toho2020_0202w.pdf",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Seems corrupt",
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
                        "https://web.archive.org/web/20200224140724/http://www.puniket.com/cirno/",
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
            dates="2020.02.02",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20200224140724/http://www.puniket.com/cirno/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20200210101842/http://www.puniket.com/aka/toho2020w_list02.htm",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="At 東方合同イベント2020冬！, which featured 紅のひろば１８, このはな咲夜１３, ようせいげんき！１３, 恋のまほうは魔理沙におまかせ！１２, 七色魔女の人形舞踏会。１０＆七曜魔女の舞踏会。１０, 旧地獄温泉 お燐の湯, もりや神社例大祭 九, みょうれんパーティー６, ゆゆみょん!８, 八雲のヒミツ基地５ and 萃香粋酔５（すいかすいすい）.",
            # comments=None,
            last_edited="2026.08.22",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 14  # ==== youseigenki14 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "14_cirno_top14_01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20210729132933/http://www.puniket.com/cirno/",
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
                        "https://web.archive.org/web/20210729132933/http://www.puniket.com/cirno/",
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
            dates="2021.01.24",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20210729132933/http://www.puniket.com/cirno/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    'Participating circles (date matches, not event name "ようせいげんき！13" that should have been ようせいげんき！14): https://web.archive.org/web/20210113043127/http://www.puniket.com/aka/toho2021w_list02.htm',
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="At 東方合同イベント2020冬！, which featured 紅のひろば１８, このはな咲夜１３, ようせいげんき！１３, 恋のまほうは魔理沙におまかせ！１２, 七色魔女の人形舞踏会。１０＆七曜魔女の舞踏会。１０, 旧地獄温泉 お燐の湯, もりや神社例大祭 九, みょうれんパーティー６, ゆゆみょん!８, 八雲のヒミツ基地５ and 萃香粋酔５（すいかすいすい）",
            # comments=None,
            last_edited="2026.08.22",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 15  # ==== youseigenki15 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "15_cirno_top15_01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20220604060245/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by HAM（points)",
            ),
            Medium(
                "15_toho2022w_zumen.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20220130142949/http://www.puniket.com/touhou/toho2022w_zumen.pdf",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
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
                        "https://web.archive.org/web/20211125192238/http://www.puniket.com/cirno/",
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
            dates="2022.01.30",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20211125192238/http://www.puniket.com/cirno/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20220114032621/http://www.puniket.com/touhou/toho2022w_list01.htm or https://web.archive.org/web/20220127233656/http://www.puniket.com/touhou/toho2022w_list02.htm",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="At 東方合同イベント2022新年！, which featured 紅のひろば２０, このはな咲夜１５, ようせいげんき！１５, 恋のまほうは魔理沙におまかせ！１４, 七色魔女の人形舞踏会。１２＆七曜魔女の舞踏会。１２, 旧地獄温泉 お燐の湯, もりや神社例大祭 十一, みょうれんパーティー８, ゆゆみょん!１０, 八雲のヒミツ基地７ and 萃香粋酔７（すいかすいすい）",
            # comments=None,
            last_edited="2026.08.23",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 16  # ==== youseigenki16 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "16_cirno_top16_01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20230718063821/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by HAM（points)",
            ),
            Medium(
                "16_230226_tohou2023w2.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20240701091029/http://www.puniket.com/touhou/230226_tohou2023w2.pdf",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.4471499, 139.6432575),
                address="2 Yamashitacho, Naka Ward, Yokohama, Kanagawa 231-0023, Japan",
                description="横浜産貿ホールマリネリア",
                sources=[
                    Source(
                        "https://web.archive.org/web/20230718063821/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                # comments=None,
                imageUrl="https://lh3.googleusercontent.com/gps-cs-s/AHRPTWn3j0r7jhTBvDEmCgBnlhwXrSYHHrkl3fqXnrZDIY8cCVr146rAAv7f4-86On8aWyTCrywzJEL_vYeMyux_gNF4fW3166cMPmdL8k1ZZiWV5_1TOMRlOt6LiAbYpurFO0j4Gw06wg=w408-h272-k-no",
                url="https://maps.app.goo.gl/QB2yHxZahKtTi3Sk7",
            ),
        ]
        event = Event(
            aliases=[
                f"ようせいげんき！{i}",
                f"Yousei Genki! {i}",
            ],
            dates="2023.02.26",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20230718063821/http://www.puniket.com/cirno/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20230319233813/http://www.puniket.com/touhou/toho2023w_list02.htm",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="At 東方合同イベント2023冬！, which featured 紅のひろば２１, このはな咲夜１６, ようせいげんき！１６, 恋のまほうは魔理沙におまかせ！１５, 七色魔女の人形舞踏会。１３＆七曜魔女の舞踏会。１３, 旧地獄温泉 お燐の湯, もりや神社例大祭 十二, みょうれんパーティー９, ゆゆみょん!１１, 八雲のヒミツ基地８ and 萃香粋酔８（すいかすいすい）.",
            # comments=None,
            last_edited="2026.08.23",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 17  # ==== youseigenki17 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "17_cirno_top17_01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20240912164712/http://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by HAM（points)",
            ),
            Medium(
                "17_touhou2024w_zumen.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20240204115605/http://www.puniket.com/touhou/touhou2024w_zumen.pdf",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            Medium(
                "17_toho2024w_cut.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20240204115605/http://www.puniket.com/touhou/toho2024w_cut.pdf",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
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
                        "https://web.archive.org/web/20240912164712/http://www.puniket.com/cirno/",
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
            dates="2024.01.28",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20240912164712/http://www.puniket.com/cirno/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20240204115609/http://www.puniket.com/touhou/toho2024w_list02.htm",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="At 東方合同イベント2024新春！, which featured 紅のひろば２２, このはな咲夜１７, ようせいげんき！１７, 恋のまほうは魔理沙におまかせ！１６, 七色魔女の人形舞踏会。１４＆七曜魔女の舞踏会。１４, 旧地獄温泉 お燐の湯, もりや神社例大祭 十三, みょうれんパーティー１０, ゆゆみょん!１２, 八雲のヒミツ基地９ and 萃香粋酔９（すいかすいすい）.",
            # comments=None,
            last_edited="2026.08.23",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 18  # ==== youseigenki18 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "18_cirno_top18_01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20250912011749/https://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by HAM（points)",
            ),
            Medium(
                "18_touhou2025w_zumen.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20250912011749/https://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            Medium(
                "18_toho2025_cut.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20250914213452/http://www.puniket.com/touhou/toho2025_cut.pdf",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
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
                        "https://web.archive.org/web/20250912011749/https://www.puniket.com/cirno/",
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
            dates="2025.02.02",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20250912011749/https://www.puniket.com/cirno/",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20250122123336/http://www.puniket.com/touhou/toho2025w_list02.htm",
                    (ReliabilityTypes.Reliable, OriginTypes.Official),
                ),
            ],
            locations=locations,
            description="At 東方合同イベント2025冬！, which featured 紅のひろば２３, このはな咲夜１８, 恋のまほうは魔理沙におまかせ！１７, 七色魔女の人形舞踏会。１５＆七曜魔女の舞踏会。１５, 旧地獄温泉 お燐の湯, もりや神社例大祭 十四, みょうれんパーティー１１, ゆゆみょん!１３, 八雲のヒミツ基地１０ and 萃香粋酔１０（すいかすいすい）.",
            # comments=None,
            last_edited="2026.08.23",
        )

        # Retrieve circles
        event.circles = retrieve_circles(event_name)
        events.append(event)

    i = 19  # ==== youseigenki19 ====
    if i in active_events:
        event_name = f"youseigenki{i}"
        print(f"Processing {event_name} ...")

        media_ = [
            Medium(
                "19_cirno_top19_01.jpg",
                [
                    Source(
                        "https://web.archive.org/web/20260602033202/https://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
                comments="Illustration by HAM（points)",
            ),
            Medium(
                "19_toho2026s_zumen.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20260602033202/https://www.puniket.com/cirno/",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            Medium(
                "19_toho2026s_cut.pdf",
                [
                    Source(
                        "https://web.archive.org/web/20260419193220/https://www.puniket.com/touhou/toho2026s_cut.pdf",
                        (ReliabilityTypes.Reliable, OriginTypes.Official),
                    )
                ],
            ),
            # Medium("",
            #        [Source("", (ReliabilityTypes.Reliable, OriginTypes.Official))]),
        ]
        locations = [
            Location(
                coordinates=(35.655153, 139.7607689),
                address="Japan, 〒105-7501 Tokyo, Minato City, Kaigan, 1 Chome−7−1 東京ポートシティ竹芝オフィスタワ",
                comments=None,
                description="都立産業貿易センター台東館７Ｆ開催",
                sources=[
                    Source(
                        "https://web.archive.org/web/20260602033202/https://www.puniket.com/cirno/",
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
            dates="2026.03.20",
            circles=[],
            media=media_,
            sources=[
                Source(
                    "Date: https://web.archive.org/web/20260602033202/https://www.puniket.com/cirno/",
                    (RT.Reliable, OT.Official),
                ),
                Source(
                    "Participating circles: https://web.archive.org/web/20260602033112/https://www.puniket.com/touhou/toho2026s_list02.htm",
                    (RT.Reliable, OT.Official),
                ),
            ],
            locations=locations,
            description="At 東方合同イベント2026春！, which featured 紅のひろば２４, このはな咲夜１９, ようせいげんき！１９, 恋のまほうは魔理沙におまかせ！１８, 七色魔女の人形舞踏会。１６＆七曜魔女の舞踏会。１６, 旧地獄温泉 お燐の湯, もりや神社例大祭 十五, みょうれんパーティー１２, ゆゆみょん!１４, 八雲のヒミツ基地１１ and 萃香粋酔１１.",
            # comments=None,
            last_edited="2026.08.23",
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
    #         last_edited="2026.08.23",
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
        last_edited="2026.08.23",
    )

    print(f"Saving {Path(__file__).stem} database...")
    event_group.save(PATH_EVENT_GROUP, indent=None)
    print("Done")
