# 3D Solutions Program

**Information now travels efficiently. Wood still doesn’t.**

**Can better-defined demand make a small amount of manufacturing worthwhile in an existing local yard, and turn more ideas into projects and more work into local income?**

3D Solutions LLC · Greensboro, North Carolina

## The North Carolina question

North Carolina didn't run out of trees. It lost much of the work that turned those trees into useful products — and the paychecks that came with it.

Furniture-factory employment fell **59.4% between 1993 and 2022** ([NC Commerce](https://www.commerce.nc.gov/news/the-lead-feed/not-your-grandfathers-manufacturing)). Beyond furniture, a [North Carolina Forest Service assessment](https://www.ncagr.gov/divisions/nc-forest-service/ncforest-assessment-chapter4/download?attachment=) records forest-industry-related employment from roughly **120,000 in 1990 to 77,000 in 2008**. Sawmill companies fell from **229 in 2001 to the low 130s** by the late 2010s, amid closures and mergers ([NC State Extension](https://content.ces.ncsu.edu/the-north-carolina-sawmill-industry-a-closer-look)). That measures companies, not a matching decline in jobs or output.

Those losses have addresses. In 2024, Weyerhaeuser curtailed its New Bern lumber mill in Vanceboro, affecting **73 workers** ([North Carolina WARN record](https://www.commerce.nc.gov/data-tools-reports/labor-market-data-tools/workforce-warn-reports/report-workforce-warn-listings-2024/open)). In 2026, Prepac announced the closure of its Whitsett plant near Greensboro; its [March WARN notice](https://www.commerce.nc.gov/data-tools-reports/labor-market-data-tools/workforce-warn-reports/report-workforce-warn-summary-list-2026) identified **200 permanent layoffs**. This is not only a story about jobs lost decades ago.

North Carolina still grows, cuts, and ships wood. Its forest sector directly employed about **66,508 people in 2024**, supporting **140,919 jobs** including indirect and induced effects. Forest-sector output rose **3.1%** while total supported employment fell **1.9%** ([NC State Extension](https://content.ces.ncsu.edu/economic-contribution-of-the-forest-sector-in-north-carolina)). More economic output is not necessarily more people earning a living from the wood. These estimates are separate from factory and forest-industry employment counts.

**What if the cost curves that pulled manufacturing toward concentration have changed enough to make some of that work worthwhile closer to home?**

Scale, costs, trade, and technology shaped manufacturing investment. Expensive engineering, job preparation, machine controls, CAD/CAM systems, and specialist programming favored facilities with volume to spread those costs. Wood could travel for processing and return as finished products because concentration made economic sense.

But the cost of moving *information* has changed. Customers use devices to describe, select, and change what they want. Computing, communication, servo control, and modular automation have become more accessible. Registered machine functions and reusable software can absorb interpretation and programming otherwise repeated on each small order. The equipment needs engineering, qualification, and maintenance. What need not recur is CAD/CAM programming for **each** accepted order.

**The important cost reduction may not be the price of making a cut. It may be the cost of getting from the customer's idea to a cut worth making.**

The [National Academies' 2024 smart-manufacturing study](https://www.nationalacademies.org/read/27260/chapter/7) describes distributed manufacturing at smaller scales. A [NIST industry review](https://www.nist.gov/publications/industry-review-distributed-production-discrete-manufacturing) examines coordination and repeated preparation burdens. Neither proves lumberyard economics. This Program tests them against alternatives.

A local yard has material, handling equipment, customers, suppliers, and people who know the business. Information can reach wood on the rack; components need not travel through a distant manufacturing chain. This is not a proposal to outproduce a large furniture factory. **Modest, bounded local automation may accommodate a significant share of otherwise avoided woodwork** — one board, one opening, one customer's result.

**What if the information reached local wood and modest automation first?** [▶ Open the working demonstration](https://system-candidate-production.up.railway.app/) and see the customer's definition reach Store evaluation, stock selection, modeled cut, mill, and drill operations, and a calculated price. The work, and some of the income, could happen closer to home.

**The customer writes the definition. Nobody at the yard interprets the project or programs the order.**

In a typical CNC workflow, each job requires interpretation, programming, and machine-specific instructions. The architecture is documented in George Platt's two issued patents, *Method and System for Consumer Home Projects Ordering and Fabrication* ([US 9,720,401 B2](https://github.com/GeorgePlattDemo/store-zero/blob/main/docs/patents/US9720401B2.pdf) and [US 10,768,609 B2](https://github.com/GeorgePlattDemo/store-zero/blob/main/docs/patents/US10768609B2.pdf)). [Store's claim-by-claim engineering correspondence](https://github.com/GeorgePlattDemo/store-zero/blob/main/STORE-ZERO-MASTER.md#2-invention-and-issued-patents) traces all **33 issued claims** to current software, candidate machinery, and remaining physical evidence. The architecture is defined and mapped; its implementation and validation are the work underway.

The machine, material, and permitted operations are registered in advance: tools, stations, reference positions, and limits, matched to yard stock. A customer defining work against those capabilities defines what becomes the machine program. System derives the job's geometry and meaning; Store independently resolves stock, supported operations, modeled time, and Q. The accepted plan lowers against a registered machine configuration without redrawing the part or reselecting stock. **Reusable controller-specific instruction generation and physical commissioning remain to be completed.**

The question is not whether the architecture can be described or the digital path demonstrated. It is whether eliminating repeated job preparation makes the *complete physical service* worthwhile.

This Program's proposition is **distributed manufacturing at the scale of an existing yard, beginning with a bounded service that could earn its keep.** The next increment is a small dimensional-stock cell, local controller integration, and inspected physical parts.

## Make the project easier to start

A person needs a fitted shelf, a replacement brace, a panel with an opening, or pieces for a small assembly. They can picture the result. Getting suitable material and accurately prepared parts is the hard part. Arranging the work can cost more effort than the work itself.

The opportunity begins upstream of the machine: help people define what they want and ask a local business what it can supply. The customer takes home pieces they can build with. The yard sells both the wood and the work that makes it useful.

Some projects could be served better. Others stay ideas because getting the right pieces feels too hard. Both must pay off: useful to the customer, worthwhile for the yard.

A defined request moves through the application to Store evaluation, material selection, modeled whole-job price, machine time, and virtual operations. The remaining question is physical execution: can the same definition move from customer request to inspected component without repeated reconstruction, separate machine programming, or manual reinterpretation?

**Define it once. Nobody downstream should have to redraw it.**

The tools and controls are familiar. The change is where job preparation happens — and how often.

## What would make it worthwhile

The smallest useful cell is set by actual requests and the full cost of supplying them: material, clarification, preparation, handling, programming, processing, inspection, people, maintenance, investment, space, and realistic utilization. Compare the **same required result** with a yard service, manual operation, local shop, supplier, or standard product that may serve the customer better.

The [Supervised Laboratory Dimensional Cell Trial](SUPERVISED-LABORATORY-CELL-TRIAL.md) follows real requests through the complete job. It compares the full chain — definition, programming, handling, processing, inspection, rework, and fulfillment — against conventional alternatives and Scan-to-Build. Reusable registration, controller integration, and maintenance count as costs, even if per-order programming falls. Count unsupported and abandoned requests as well as completed work. A good result is useful work supplied at a worthwhile margin. A useful negative identifies what stands in the way.

The experiment is not whether wood can be cut locally. **It is whether putting better information in front of a modest, registered machine changes the economics of supplying useful parts.**

## Three connected homes

| **Repository** | **The question it answers** |
| --- | --- |
| **Program** | Why pursue this, and what would make it viable? Research, evidence, candidate engineering, and development decisions. |
| [**System**](https://github.com/GeorgePlattDemo/new-system) | How does an idea become an identified job? The application, shared job meaning, translation, customer decision, and records. |
| [**Store**](https://github.com/GeorgePlattDemo/store-zero) | What can this yard provide? Material, registered capability, complete operation planning, modeled work, economics, and attributable answers or refusals. |

## What has been shown

The [working application](https://system-candidate-production.up.railway.app/) is an operational software prototype, not a drawing of a proposed one. Try **Start your own**: Intent establishes the job's requirements; the Bench lets you work their values. Then follow the [Project 1 current digital manufacturing proof](https://github.com/GeorgePlattDemo/store-zero/blob/main/PROJECT-1-CURRENT-DIGITAL-MANUFACTURING-PROOF.md) through identified demand, independent manifest, fresh Store evaluation, simulated acceptance, bound job packet, registered lowering, and virtual replay. The [verification record](https://github.com/GeorgePlattDemo/new-system/blob/main/SYSTEM-MASTER.md#14-testing-and-verification) identifies the tested scope and remaining obligations.

A 16-inch SPF definition produces **Q $8.62**; a changed 18-inch definition produces **Q $9.13**, selecting a different stock parent and changed operation geometry. A separate Store reference with independently selected spot locations and depths produces **Q $9.16**. These are identified, modeled manufacturing results, not three real customer purchases or production releases. Unsupported work must receive an attributable refusal rather than a made-up favorable answer.

The application demonstrates the digital definition-to-manufacturing path. Store Zero's prices and machine time are modeled; physical D-001/S-001 machines have not been commissioned. The next proof is reusable controller export, controlled material movement, safe local operation, measured time, and **inspected wood components**. A working compiler model is not proof that a machine has made the part.

- [Evidence](EVIDENCE.md) connects the North Carolina record, manufacturing research, patents, and digital implementation to their sources.
- [Supervised Laboratory Dimensional Cell Trial](SUPERVISED-LABORATORY-CELL-TRIAL.md) defines the candidate machine, supervised physical qualification, comparisons, and full-job economics.

## Bring a real case

Bring one request a yard keeps turning away, or one project someone would start if the right pieces were available.

- **Customers** can establish the need and what they would pay.
- **Dealers** can establish service demand and operating realities.
- **Workers and educators** can examine the tasks and skills.
- **Engineers** can test the capability; **researchers** can compare the complete economics.
- **Economic-development, extension, and community partners** can help establish whether the service creates additional local value or shifts existing work, who can participate, and what training or support would make a bounded test practical.

[Bring a case, question, or observation](https://github.com/GeorgePlattDemo/3d-solutions-program/discussions/1), or share these repositories with someone who can test part of the proposition.

*Information before atoms. NO BLOOD ON WOOD.*

Maintainers: [AGENTS.md](AGENTS.md) · [Shared definitions](https://github.com/GeorgePlattDemo/new-system/blob/main/docs/DEFINITIONS.md)
