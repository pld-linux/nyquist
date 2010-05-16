Summary:	Nyquist - a language for composition and sound synthesis
Summary(pl.UTF-8):	Nyquist - język do komponowania i syntezy dźwięku
Name:		nyquist
Version:	2.31
Release:	1
License:	BSD
# but "Please do not distribute modified versions of Nyquist without permission."
Group:		Applications/Sound
Source0:	http://www-2.cs.cmu.edu/~music/nyquist/nyqsrc231.zip
# Source0-md5:	49ff7053ce76b11f61685f22fd068928
Patch0:		%{name}-opt.patch
URL:		http://www-2.cs.cmu.edu/~music/nyquist/
BuildRequires:	libstdc++-devel
BuildRequires:	readline-devel
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nyquist is a language for sound synthesis and music composition.
Unlike score languages that tend to deal only with events, or signal
processing languages that tend to deal only with signals and
synthesis, Nyquist handles both in a single integrated system. Nyquist
is also flexible and easy to use because it is based on an interactive
Lisp interpreter.

With Nyquist, you can design instruments by combining functions (much
as you would using the orchestra languages of Music V, cmusic, or
Csound). You can call upon these instruments and generate a sound just
by typing a simple expression. You can combine simple expressions into
complex ones to create a whole composition.

%description -l pl.UTF-8
Nyquist to język do syntezy dźwięku i komponowania muzyki. W
przeciwieństwie do języków zapisu dążących tylko do obsługi zdarzeń
oraz języków przetwarzania dążących tylko do obsługi sygnałów i
syntezy, Nyquist obsługuje oba zagadnienia w jednym, zintegrowanym
systemie. Nyquist jest także elastyczny i łatwy w użyciu, ponieważ
jest oparty na interaktywnym interpreterze Lispu.

Przy użyciu Nyquista można projektować instrumenty poprzez łączenie
funkcji (podobnie jak robi się to w językach orkiestrowych Music V,
cmusic lub Csound). Można odwoływać się do tych instrumentów i
generować dźwięki poprzez wpisywanie prostych wyrażeń. Można łączyć
proste wyrażenia w bardziej złożone, aby utworzyć całą kompozycję.

%prep
%setup -q -n %{name}
%patch0 -p1
ln -s sys/unix/linux/Makefile Makefile

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install ny $RPM_BUILD_ROOT%{_bindir}
cp -rf runtime lib demos test $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme.txt advantages.txt license.txt todo.txt doc/*
%attr(755,root,root) %{_bindir}/ny
%{_datadir}/%{name}
