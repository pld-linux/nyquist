Summary:	-
Summary(pl):	-
Name:		nyquist
Version:	2.29
Release:	0.1
License:	BSD
# but "Please do not distribute modified versions of Nyquist without permission."
Group:		Libraries
Source0:	http://www-2.cs.cmu.edu/~music/nyquist/nyquist229.zip
# Source0-md5:	5afea86c994bbd4597397c6ecdc40872
URL:		http://www-2.cs.cmu.edu/~music/nyquist/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
