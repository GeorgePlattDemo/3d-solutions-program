# 3D Solutions Program

**Information travels anywhere. Wood doesn't. What happens when you send one to the other?**

<a href="https://georgeplattdemo.github.io/scan-to-build-system/system-build-current.html"><kbd>▶ OPEN THE WORKING APP</kbd></a>

3D Solutions LLC · Greensboro, North Carolina  
U.S. Patents [9,720,401 B2](https://github.com/GeorgePlattDemo/scan-to-build-system/blob/main/docs/patents/source/US9720401B2.pdf) and [10,768,609 B2](https://github.com/GeorgePlattDemo/scan-to-build-system/blob/main/docs/patents/source/US10768609B2.pdf)

---

## The gap in the middle

Walk into an independent lumberyard and ask for something that fits the odd corner of your house. You'll meet a tape measure, a pencil, a practiced eye and a saw. It works, one conversation at a time.

At the other end of the spectrum, researchers are taking robots into the woods, scanning irregular stems and cutting each one to its own shape. That works too, at a very different scale.

In between, the job usually leaves town. It goes to a custom shop or a factory, and the meaning of the job gets rebuilt at every handoff along the way.

This program asks about that middle:

> **Can better-defined demand, sent to wood already sitting in a yard, make a small amount of local processing worth doing — without turning the yard into a factory?**

A yes would mean more of the value of a wood project stays with the wood, the yard and the people already there. A no is a useful answer too.

## Why now

The edge is already moving toward the material:

- Mallegol, Rohart & Champroy (2026), *The Tree Dictates the Shape*, Construction Robotics 10:30. [doi:10.1007/s41693-026-00188-y](https://doi.org/10.1007/s41693-026-00188-y) — eighteen months of adaptive robotic fabrication beside underused chestnut in rural France.
- Nahmad Vazquez, Garivani & Dackiw (2024), *Decentralized, Data-Informed, Robotic-Based Digital Timber Micro-Factories*, Construction Robotics 8:24. [doi:10.1007/s41693-024-00132-y](https://doi.org/10.1007/s41693-024-00132-y) — small, near-site timber manufacturing with local material and labor.

And North Carolina has a reason to care:

- Parajuli & Bardon (2026), *Economic Contribution of the Forest Sector in North Carolina, 2024*, NC State Extension AG-844 — about $25.4 billion in direct output and 66,500 direct jobs, with output up and employment down.
- Sodiya, Parajuli, Abt & Gray (2023), *Spatial Analysis of Forest Product Manufacturers in North Carolina*, Forest Science 69(1). [doi:10.1093/forsci/fxac045](https://doi.org/10.1093/forsci/fxac045) — where the state's primary and secondary wood manufacturers sit relative to the forest.

Where higher-value wood work happens, and who gets to do it, is a live question in published and ongoing research. This program works the same question from the yard's side of the counter.

## The patents drew the whole path first

The issued patents — *Method and System for Consumer Home Projects Ordering and Fabrication*, granted in 2017 and 2020 — describe the entire path as one system:

- a person defines a wood project through an interface, choosing and sizing from sheet goods or dimensional lumber;
- a retail store supplies the material and the estimated price;
- a tandem machine — one side for boards, one for sheets — positions the stock with servo-driven rollers against a fence, clamps it, and cuts, drills and routes it;
- labeled parts go back to the customer for pickup.

When those were written, the pieces were expensive or missing. They aren't anymore. Phones capture rooms. Open-source motion control runs real machines. Off-the-shelf servo and motion boards are catalog items. Language models can help a person say what they mean without taking over what gets decided.

What's left is to show each piece working, in order. That's what the other two repositories do.

## Two halves, working

| | What it proves | Patent part it makes concrete |
| --- | --- | --- |
| [**Scan-to-Build System**](https://github.com/GeorgePlattDemo/scan-to-build-system) | A project defined once can travel to a yard and back without anyone redrawing it. | The customer interface, the project definition, the record |
| [**Scan-to-Build Store**](https://github.com/GeorgePlattDemo/scan-to-build-store) | A yard can answer that project from its own stock, prices and machine — yes, no, or not yet, with reasons. | The store, its material and price, the machine |

They are deliberately separate. System never invents a Store answer, and Store never rewrites the customer's project. If one program did both jobs, nothing would really have crossed from the customer to the yard.

The working app ties them together: a project built in System is priced and answered live by a separately hosted Store.

## The stages

| Stage | What it is | Where it stands |
| --- | --- | --- |
| **1 — One board** | One roller moves one board between two fixed saws and cuts it to a defined length. Deliberately simple: the test is whether the job reaches the saw without being redrawn, not whether a saw can cut wood. | Works in software |
| **2 — Reference yard, reference cell** | A fictional but fully specified yard (Store Zero) answers real project requests. Its cell is designed as two rollers, two saws, three routers — two on clean axes, one end mill — and two spot drills. | Works in software; machine time is modeled |
| **3 — Physical cell** | A real build on off-the-shelf parts and open-source control, with guarding and measured cycles. | Next |
| **4 — Evidence-informed system** | Demand, refusals, measured cycles, material behavior and economics decide what the mature yard and cell should become. The patents' full machine is the upper bound being tested — the data may justify some of it, all of it, or none. | Not predetermined |

Details live in the [Store stage guide](https://github.com/GeorgePlattDemo/scan-to-build-store/blob/main/STB-STORE-CELL-STAGES-0.1.md).

## Who might find something here

- **Independent yards** — new work from stock you already paid to hold, without handing your business to someone else's software.
- **Forestry and extension** — ordinary and regional lumber stays ordinary until a real job justifies changing it, and what's left of every board is tracked.
- **Machine builders** — a bounded cell built from parts you can order, not a new machine to invent.
- **Workforce and community colleges** — as machines get more bounded and information gets better, what human work remains, and what new work appears?
- **Small-business and economic development** — a small existing business becoming more capable, rather than less necessary.

Each of those is a question, not a promise. That's the point of the research.

## Where the support lives

| If you want to know… | Read | Why it's the evidence |
| --- | --- | --- |
| Is incomplete demand really useful information? | [Demand as architecture](research/demand-as-architecture.md) | The research proposition, and where it's allowed to stop |
| What's the first physical experiment? | [Bounded cell trial](research/bounded-cell-trial.md) | One board, two saws, candidate parts, what to measure |
| How would the machines actually get built? | [Machine development](research/machine-development/README.md) | Build phases, engineering notes, sheet and board machines |
| What do the patents actually disclose? | [Patent sources](https://github.com/GeorgePlattDemo/scan-to-build-system/blob/main/docs/patents/README.md) | The issued grants and how the current work maps to them |
| Does the digital path actually work? | [System verification register](https://github.com/GeorgePlattDemo/scan-to-build-system/blob/main/docs/project/VERIFICATION-REGISTER.md) | Each claim tied to a test and an exact version |
| What can a yard actually answer? | [Store Zero](https://github.com/GeorgePlattDemo/scan-to-build-store/blob/main/STORE-ZERO.md) | The reference yard, its stock, prices and refusals |
| Who decides what? | [Authority register](governance/authority.md) | Which repository owns which facts |

## The fine print

The app is a working software proof, not a store. Store Zero is a fictional yard; its prices are budgetary estimates, not quotes. Machine times are modeled. No machine has been commissioned yet. Publication here grants no patent license.

**Information before atoms. NO BLOOD ON WOOD.**

<sub>Maintainers: [`AGENTS.md`](AGENTS.md) · [`governance/semantic-provenance.md`](governance/semantic-provenance.md) · [`migration/`](migration/) · `python3 tools/check_program.py`</sub>
