# ANARCHY Research Source Bundle — 2026-09-07

**Status:** Source registry / historical prior art
**Purpose:** Preserve and classify the external references supplied during the ANARCHY research pass. These sources are evidence and prior art, not ANARCHY dependencies.

## Source inventory

| Source | Classification | ANARCHY relevance |
|---|---|---|
| Apache/mod_perl offsite article index | web/application ecosystem history | Demonstrates how technical knowledge, printed media, online articles, Apache, Perl, and community documentation formed a distributed knowledge layer. |
| TLDP Text-Terminal-HOWTO | interface / terminal architecture | Documents physical terminals, emulation, pseudo-terminals, `/dev/tty`, terminfo, SSH/Telnet, serial links, thin clients, and terminal configuration. |
| MiSTer FPGA Forum thread `t=8587` | community/hardware evidence | Preserve as a community reference; exact thread contents could not be independently retrieved during this pass because the forum endpoint rejected automated access. Do not infer its topic until captured. |
| BSD Magazine 09/2013 PDF | BSD/live-media/installation/admin prior art | Contains concrete material on custom Live CDs, USB media, package inclusion, installation media, mirrors, modular installers, storage, encryption, monitoring, and virtualization. |
| Yumpu Italian magazine archive page | historical magazine index | Preserve as a discovery/provenance pointer; automated retrieval failed during this pass, so metadata should remain unverified until independently captured. |
| Internet Archive `LnC39` | Linux & C. / coverdisc archive | Direct historical artifact evidence: Linux & C. issue 39, Dynebolic Linux 1.3, FreeSBIE 1.0, FreeBSD 5.2.1, Mandrake 10, OpenOffice 1.1.1, and multiple kernel source trees. |
| dyne:bolic manual at ibiblio | primary historical documentation | Documents live booting, docking, modular software, network/USB/hard-disk boot, cluster farms, live-CD customization, software-module creation, multimedia pipelines, and community/free-software philosophy. |

## 1. Apache / Perl / mod_perl knowledge ecosystem

The Apache mod_perl offsite index explicitly catalogs articles in printed and online media and includes a historical entry for **Linux & C.**: March–July 2002, "Apache/mod_perl: an application server open source," by Enrico Sorcinelli, with five tutorial articles. This is strong evidence that Linux & C. was not merely a general Linux magazine; it carried material about Apache/Perl integration and open-source web application infrastructure.

The page also records coverage in The Perl Journal, Sys Admin Magazine, BYTE, Linux Journal, Linux Magazin, Perl.com, ApacheToday/ServerWatch, ApacheWeek, Developer Shed, and others. The important ANARCHY lesson is the **distributed technical knowledge graph** surrounding open infrastructure: projects were implemented in code, explained in magazines/howtos, discussed in communities, and republished across media.

### ANARCHY interpretation

```text
open implementation
       |
       +--> project documentation
       +--> HOWTOs / manuals
       +--> magazines / printed media
       +--> online articles
       +--> community discussion
       |
       v
portable technical knowledge
```

The Apache/mod_perl page states that its purpose is to partially cover resources and invites additional references, making it useful as an example of a project-maintained external bibliography.

## 2. Terminal, console, and thin-client substrate

The TLDP Text-Terminal-HOWTO is a major historical interface reference. It distinguishes real text terminals from terminal emulation and covers Linux consoles, serial terminals, pseudo-terminals, `/dev/tty`, terminfo/termcap, SSH/Telnet, terminal servers, flow control, keyboard/display behavior, and thin clients.

This matters to ANARCHY because a hierarchy-free network does not necessarily require a graphical desktop at every node. A node can expose capability through a text console, serial connection, pseudo-terminal, remote shell, or thin-client interface.

### Architectural extraction

```text
physical terminal
      |
serial / network transport
      |
terminal protocol / PTY
      |
console or shell
      |
node capability interface
```

Terminfo is especially relevant as an example of an interface-description database used to mediate differences between terminal capabilities and applications.

## 3. BSD Magazine 09/2013 — live media and installation architecture

The supplied BSD Magazine PDF contains unusually direct prior art for ANARCHY's live/distribution model.

The issue's contents include **MidnightBSD Custom Installations and Live CDs**. The article describes:

- `release` and `nrelease` build trees;
- building installation media and Live CDs/USB media;
- customizing `/usr/src/nrelease/root`;
- inserting configuration files into staged media;
- installing packages into the destination environment;
- building ISO images;
- producing flash images;
- rebuilding release media from source;
- bsdinstall as a modular installation mechanism composed of smaller programs/scripts;
- package indexes embedded in installation media;
- local/private mirrors through modified package-index URLs.

This is directly relevant to the ANARCHY separation between **system construction**, **installation media**, **package metadata**, **execution backend**, and **target environment**.

The same issue also covers server maintenance, monitoring, ZFS, PEFS directory encryption, and FreeBSD on XenServer. The ZFS material describes pooled storage, snapshots, clones, checksums, and RAID-Z; the PEFS article demonstrates stacked filesystem encryption without requiring a user-level daemon; the XenServer article explicitly frames virtualization in terms of administration, provisioning, and delivery times.

### ANARCHY interpretation

```text
source tree
   |
   +--> buildworld / buildkernel
   |
   +--> release / nrelease
   |
   +--> package index + package set
   |
   +--> ISO / USB / installation media
   |
   v
portable deployment artifact
```

This is important corroborating evidence for the existing ANARCHY `installation-and-distribution-model.md` research.

## 4. Linux & C. issue 39 — the strongest new historical artifact

The Internet Archive record identifies the artifact as **Linux & C. Magazine — n. 39**, an Italian magazine dedicated to open-source software, mostly Linux.

The coverdisc archive identifies:

- CD1: **Dynebolic Linux 1.3**
- CD2: **FreeSBIE 1.0**
- DVD: **FreeBSD 5.2.1** (bootable)
- Mandrake 10 Official Release disc images
- OpenOffice 1.1.1
- Linux kernel source trees for 2.6.5, 2.4.26, 2.2.26, and 2.0.40

The archive exposes the original ISO images and cover images. This turns Linux & C. from a secondary magazine reference into a **recoverable software-distribution artifact**.

### Why this is important to ANARCHY

Issue 39 provides evidence of a historical distribution ecosystem where a magazine acted as a physical/software aggregation layer:

```text
Linux & C. editorial layer
          |
          +--> Dynebolic 1.3
          +--> FreeSBIE 1.0
          +--> FreeBSD 5.2.1
          +--> Mandrake 10
          +--> OpenOffice
          +--> kernel source trees
          |
          v
     physical/digital distribution
```

This should be treated as **provenance evidence**, not as proof that these projects shared a technical architecture. The value is the contemporaneous packaging and distribution context.

## 5. dyne:bolic manual — live, docked, modular, networkable

The historical dyne:bolic manual describes the system as a live bootable GNU/Linux distribution running directly from CD and emphasizes multimedia production. It also documents an unusual installation strategy called **docking**: running from hard disk by copying a directory rather than repartitioning the disk.

The manual's table of contents explicitly includes:

- data volumes;
- home/settings nesting;
- hard-disk installation/docking;
- extra software modules;
- boot from hard disk;
- boot from network;
- boot from USB;
- cluster computer farms;
- data safety;
- customization of the live CD;
- creation of new software modules.

The manual also describes chaining applications through JACK/ALSA and includes low-bandwidth streaming approaches, including text/ASCII-oriented video through Hasciicam.

### ANARCHY interpretation

The most valuable abstraction is not the specific multimedia application set. It is the **composable live environment**:

```text
base live system
      |
      +--> persistent/user data
      +--> optional modules
      +--> local hardware
      +--> network boot
      +--> USB boot
      +--> hard-disk docking
      +--> cluster/node operation
      |
      v
portable node environment
```

This reinforces the existing ANARCHY distinction between a live artifact, an installation description, and the target system.

## 6. MiSTer FPGA forum reference

The supplied URL points to a MiSTer FPGA forum topic. The automated endpoint currently rejects retrieval of that exact topic, while the forum itself is reachable through indexed pages.

**Evidence status:** unresolved.

Do not assign technical meaning to this source until the exact topic is captured manually, archived, or supplied as an export/screenshot. Once captured, record:

- topic title;
- author;
- date;
- replies;
- referenced repositories;
- hardware/core names;
- build instructions;
- URLs;
- attached files/images;
- relevant licenses;
- SHA-256 hashes for any downloaded artifacts.

## 7. Yumpu magazine archive reference

The supplied Yumpu URL appears to be an Italian magazine-archive discovery page. Automated retrieval failed during this pass.

**Evidence status:** discovery pointer only.

Do not copy bibliographic facts from the URL slug into the ANARCHY corpus until the page or an underlying scan is independently recovered.

## 8. Cross-source synthesis

These sources strengthen a common historical pattern already emerging in the ANARCHY corpus:

```text
                    KNOWLEDGE / PROVENANCE
                            |
              +-------------+-------------+
              |                           |
       magazines / HOWTOs          project manuals
              |                           |
              +-------------+-------------+
                            |
                     SYSTEM KNOWLEDGE
                            |
       +--------------------+--------------------+
       |                    |                    |
   live media          package/install       interfaces
       |                    |                    |
 dyne:bolic          BSD release/nrelease   terminals/PTY
 Puredyne            package indexes        terminfo
 FreeSBIE            local mirrors          SSH/serial
       |                    |                    |
       +--------------------+--------------------+
                            |
                      NODE ARTIFACT
                            |
                 portable / reproducible
                    administrator-controlled
                            |
                            v
                         ANARCHY
```

## 9. Research rules for these sources

1. Preserve source URLs and retrieval dates.
2. Prefer primary artifacts over secondary summaries.
3. Preserve magazine scans, coverdisc ISOs, manuals, and source archives when legally permitted.
4. Hash recovered artifacts before analysis.
5. Record exact release/version numbers.
6. Separate historical facts from architectural interpretation.
7. Do not infer licenses from absence of visible license text.
8. Do not treat a magazine's bundling decision as evidence of technical dependency.
9. Treat inaccessible links as unresolved provenance pointers rather than filling gaps by inference.

## Primary references

- Apache mod_perl offsite article index: https://perl.apache.org/docs/offsite/articles.html
- TLDP Text-Terminal-HOWTO: https://tldp.org/HOWTO/html_single/Text-Terminal-HOWTO/
- MiSTer FPGA forum topic: https://misterfpga.org/viewtopic.php?t=8587
- BSD Magazine PDF: https://www.sysadmin.org.mx/sites/sysadmin.mx/files/bsd_09_2013_0.pdf
- Yumpu Italian magazine archive pointer: https://www.yumpu.com/it/document/view/10845213/da-mirella-edicola-archivio-riviste-riviste-presenti-7393-rivista-
- Linux & C. issue 39 archive: https://archive.org/details/LnC39
- dyne:bolic historical manual: https://distro.ibiblio.org/dynebolic/dynebolic-manual.txt
