#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kmouth
Version  : 23.04.3
Release  : 56
URL      : https://download.kde.org/stable/release-service/23.04.3/src/kmouth-23.04.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.3/src/kmouth-23.04.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.3/src/kmouth-23.04.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: kmouth-bin = %{version}-%{release}
Requires: kmouth-data = %{version}-%{release}
Requires: kmouth-license = %{version}-%{release}
Requires: kmouth-locales = %{version}-%{release}
Requires: kmouth-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the kmouth package.
Group: Binaries
Requires: kmouth-data = %{version}-%{release}
Requires: kmouth-license = %{version}-%{release}

%description bin
bin components for the kmouth package.


%package data
Summary: data components for the kmouth package.
Group: Data

%description data
data components for the kmouth package.


%package doc
Summary: doc components for the kmouth package.
Group: Documentation
Requires: kmouth-man = %{version}-%{release}

%description doc
doc components for the kmouth package.


%package license
Summary: license components for the kmouth package.
Group: Default

%description license
license components for the kmouth package.


%package locales
Summary: locales components for the kmouth package.
Group: Default

%description locales
locales components for the kmouth package.


%package man
Summary: man components for the kmouth package.
Group: Default

%description man
man components for the kmouth package.


%prep
%setup -q -n kmouth-23.04.3
cd %{_builddir}/kmouth-23.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688851040
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1688851040
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kmouth
cp %{_builddir}/kmouth-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kmouth/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kmouth-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kmouth/7c203dee3a03037da436df03c4b25b659c073976 || :
cp %{_builddir}/kmouth-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/kmouth/1bd373e4851a93027ba70064bd7dbdc6827147e1 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kmouth
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kmouth
/usr/bin/kmouth

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kmouth.desktop
/usr/share/icons/hicolor/16x16/actions/phrase.png
/usr/share/icons/hicolor/16x16/actions/phrasebook.png
/usr/share/icons/hicolor/16x16/apps/kmouth.png
/usr/share/icons/hicolor/22x22/actions/phrase.png
/usr/share/icons/hicolor/22x22/actions/phrasebook.png
/usr/share/icons/hicolor/22x22/apps/kmouth.png
/usr/share/icons/hicolor/32x32/actions/phrase.png
/usr/share/icons/hicolor/32x32/actions/phrasebook.png
/usr/share/icons/hicolor/32x32/apps/kmouth.png
/usr/share/icons/hicolor/48x48/apps/kmouth.png
/usr/share/kmouth/books/ca/ca-courteousness.phrasebook
/usr/share/kmouth/books/ca/ca-greetings.phrasebook
/usr/share/kmouth/books/ca/ca-howareyou.phrasebook
/usr/share/kmouth/books/ca/ca-personal.phrasebook
/usr/share/kmouth/books/ca/ca.desktop
/usr/share/kmouth/books/de/de-courteousness.phrasebook
/usr/share/kmouth/books/de/de-greetings.phrasebook
/usr/share/kmouth/books/de/de-howareyou.phrasebook
/usr/share/kmouth/books/de/de-personal.phrasebook
/usr/share/kmouth/books/de/de.desktop
/usr/share/kmouth/books/en/en-courteousness.phrasebook
/usr/share/kmouth/books/en/en-greetings.phrasebook
/usr/share/kmouth/books/en/en-howareyou.phrasebook
/usr/share/kmouth/books/en/en-personal.phrasebook
/usr/share/kmouth/books/en/en.desktop
/usr/share/kmouth/books/sv/sv-courteousness.phrasebook
/usr/share/kmouth/books/sv/sv-greetings.phrasebook
/usr/share/kmouth/books/sv/sv-howareyou.phrasebook
/usr/share/kmouth/books/sv/sv-personal.phrasebook
/usr/share/kmouth/books/sv/sv.desktop
/usr/share/kxmlgui5/kmouth/kmouthui.rc
/usr/share/kxmlgui5/kmouth/phrasebookdialogui.rc
/usr/share/metainfo/org.kde.kmouth.appdata.xml
/usr/share/xdg/kmouthrc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kmouth/index.cache.bz2
/usr/share/doc/HTML/ca/kmouth/index.docbook
/usr/share/doc/HTML/ca/kmouth/kmouthcpref.png
/usr/share/doc/HTML/ca/kmouth/kmouthctts.png
/usr/share/doc/HTML/ca/kmouth/kmouthwizard1.png
/usr/share/doc/HTML/ca/kmouth/kmouthwizard2.png
/usr/share/doc/HTML/ca/kmouth/kmouthwizard3.png
/usr/share/doc/HTML/da/kmouth/index.cache.bz2
/usr/share/doc/HTML/da/kmouth/index.docbook
/usr/share/doc/HTML/de/kmouth/index.cache.bz2
/usr/share/doc/HTML/de/kmouth/index.docbook
/usr/share/doc/HTML/de/kmouth/kmouthcpref.png
/usr/share/doc/HTML/de/kmouth/kmouthctts.png
/usr/share/doc/HTML/de/kmouth/kmouthcwcp.png
/usr/share/doc/HTML/de/kmouth/kmouthedit.png
/usr/share/doc/HTML/de/kmouth/kmouthmain.png
/usr/share/doc/HTML/de/kmouth/kmouthwizard1.png
/usr/share/doc/HTML/de/kmouth/kmouthwizard2.png
/usr/share/doc/HTML/de/kmouth/kmouthwizard3.png
/usr/share/doc/HTML/en/kmouth/index.cache.bz2
/usr/share/doc/HTML/en/kmouth/index.docbook
/usr/share/doc/HTML/en/kmouth/kmouthcpref.png
/usr/share/doc/HTML/en/kmouth/kmouthctts.png
/usr/share/doc/HTML/en/kmouth/kmouthcwcp.png
/usr/share/doc/HTML/en/kmouth/kmouthedit.png
/usr/share/doc/HTML/en/kmouth/kmouthmain.png
/usr/share/doc/HTML/en/kmouth/kmouthwizard1.png
/usr/share/doc/HTML/en/kmouth/kmouthwizard3.png
/usr/share/doc/HTML/es/kmouth/index.cache.bz2
/usr/share/doc/HTML/es/kmouth/index.docbook
/usr/share/doc/HTML/fr/kmouth/index.cache.bz2
/usr/share/doc/HTML/fr/kmouth/index.docbook
/usr/share/doc/HTML/fr/kmouth/kmouthcpref.png
/usr/share/doc/HTML/fr/kmouth/kmouthctts.png
/usr/share/doc/HTML/fr/kmouth/kmouthedit.png
/usr/share/doc/HTML/fr/kmouth/kmouthmain.png
/usr/share/doc/HTML/fr/kmouth/kmouthwizard.png
/usr/share/doc/HTML/it/kmouth/index.cache.bz2
/usr/share/doc/HTML/it/kmouth/index.docbook
/usr/share/doc/HTML/it/kmouth/kmouthcpref.png
/usr/share/doc/HTML/it/kmouth/kmouthctts.png
/usr/share/doc/HTML/it/kmouth/kmouthcwcp.png
/usr/share/doc/HTML/it/kmouth/kmouthedit.png
/usr/share/doc/HTML/it/kmouth/kmouthmain.png
/usr/share/doc/HTML/it/kmouth/kmouthwizard1.png
/usr/share/doc/HTML/it/kmouth/kmouthwizard2.png
/usr/share/doc/HTML/it/kmouth/kmouthwizard3.png
/usr/share/doc/HTML/nl/kmouth/index.cache.bz2
/usr/share/doc/HTML/nl/kmouth/index.docbook
/usr/share/doc/HTML/nl/kmouth/kmouthcpref.png
/usr/share/doc/HTML/nl/kmouth/kmouthctts.png
/usr/share/doc/HTML/nl/kmouth/kmouthcwcp.png
/usr/share/doc/HTML/nl/kmouth/kmouthedit.png
/usr/share/doc/HTML/nl/kmouth/kmouthmain.png
/usr/share/doc/HTML/nl/kmouth/kmouthwizard.png
/usr/share/doc/HTML/pt/kmouth/index.cache.bz2
/usr/share/doc/HTML/pt/kmouth/index.docbook
/usr/share/doc/HTML/pt_BR/kmouth/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kmouth/index.docbook
/usr/share/doc/HTML/pt_BR/kmouth/kmouthcpref.png
/usr/share/doc/HTML/pt_BR/kmouth/kmouthctts.png
/usr/share/doc/HTML/pt_BR/kmouth/kmouthcwcp.png
/usr/share/doc/HTML/pt_BR/kmouth/kmouthedit.png
/usr/share/doc/HTML/pt_BR/kmouth/kmouthmain.png
/usr/share/doc/HTML/pt_BR/kmouth/kmouthwizard1.png
/usr/share/doc/HTML/pt_BR/kmouth/kmouthwizard2.png
/usr/share/doc/HTML/pt_BR/kmouth/kmouthwizard3.png
/usr/share/doc/HTML/ru/kmouth/index.cache.bz2
/usr/share/doc/HTML/ru/kmouth/index.docbook
/usr/share/doc/HTML/sv/kmouth/index.cache.bz2
/usr/share/doc/HTML/sv/kmouth/index.docbook
/usr/share/doc/HTML/sv/kmouth/kmouthcpref.png
/usr/share/doc/HTML/sv/kmouth/kmouthctts.png
/usr/share/doc/HTML/sv/kmouth/kmouthcwcp.png
/usr/share/doc/HTML/sv/kmouth/kmouthedit.png
/usr/share/doc/HTML/sv/kmouth/kmouthmain.png
/usr/share/doc/HTML/sv/kmouth/kmouthwizard.png
/usr/share/doc/HTML/uk/kmouth/index.cache.bz2
/usr/share/doc/HTML/uk/kmouth/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kmouth/1bd373e4851a93027ba70064bd7dbdc6827147e1
/usr/share/package-licenses/kmouth/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kmouth/7c203dee3a03037da436df03c4b25b659c073976

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kmouth.1
/usr/share/man/da/man1/kmouth.1
/usr/share/man/de/man1/kmouth.1
/usr/share/man/es/man1/kmouth.1
/usr/share/man/et/man1/kmouth.1
/usr/share/man/fr/man1/kmouth.1
/usr/share/man/it/man1/kmouth.1
/usr/share/man/man1/kmouth.1
/usr/share/man/nl/man1/kmouth.1
/usr/share/man/pt/man1/kmouth.1
/usr/share/man/pt_BR/man1/kmouth.1
/usr/share/man/ru/man1/kmouth.1
/usr/share/man/sv/man1/kmouth.1
/usr/share/man/uk/man1/kmouth.1

%files locales -f kmouth.lang
%defattr(-,root,root,-)

