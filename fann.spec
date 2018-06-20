%define major 2
%define libname %mklibname fann %{major}
%define devname %mklibname fann -d
%define dlibname %mklibname doublefann %{major}
%define fxlibname %mklibname fixedfann %{major}
%define fllibname %mklibname floatfann %{major}

Name: fann
Version: 2.2.0
Release: 2
Source0: https://github.com/libfann/fann/archive/%{version}.tar.gz
Patch0: fann-2.2.0-link-libm.patch
Summary: Fast Artificial Neural Network library
URL: http://github.com/libfann
License: LGPLv2.1
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja

%description
Fast Artificial Neural Network Library is a free open source neural network 
library, which implements multilayer artificial neural networks in C with 
support for both fully connected and sparsely connected networks. 
Cross-platform execution in both fixed and floating point are supported. 
It includes a framework for easy handling of training data sets. It is easy to 
use, versatile, well documented, and fast. Bindings to more than 15 programming
languages are available. An easy to read introduction article and a reference 
manual accompanies the library with examples and recommendations on how to use 
the library. Several graphical user interfaces are also available for the 
library.

%package -n %{libname}
Summary: Fast Artificial Neural Network library
Group: System/Libraries

%description -n %{libname}
Fast Artificial Neural Network Library is a free open source neural network 
library, which implements multilayer artificial neural networks in C with 
support for both fully connected and sparsely connected networks. 
Cross-platform execution in both fixed and floating point are supported. 
It includes a framework for easy handling of training data sets. It is easy to 
use, versatile, well documented, and fast. Bindings to more than 15 programming
languages are available. An easy to read introduction article and a reference 
manual accompanies the library with examples and recommendations on how to use 
the library. Several graphical user interfaces are also available for the 
library.

%files -n %{libname}
%{_libdir}/libfann.so.%{major}
%{_libdir}/libfann.so.%{major}.*0

%package -n %{dlibname}
Summary: Fast Artificial Neural Network library operating on doubles
Group: System/Libraries

%description -n %{dlibname}
Fast Artificial Neural Network Library is a free open source neural network 
library, which implements multilayer artificial neural networks in C with 
support for both fully connected and sparsely connected networks. 
Cross-platform execution in both fixed and floating point are supported. 
It includes a framework for easy handling of training data sets. It is easy to 
use, versatile, well documented, and fast. Bindings to more than 15 programming
languages are available. An easy to read introduction article and a reference 
manual accompanies the library with examples and recommendations on how to use 
the library. Several graphical user interfaces are also available for the 
library.

%files -n %{dlibname}
%{_libdir}/libdoublefann.so.%{major}
%{_libdir}/libdoublefann.so.%{major}.*0

%package -n %{fxlibname}
Summary: Fast Artificial Neural Network library using fixed-point math
Group: System/Libraries

%description -n %{fxlibname}
Fast Artificial Neural Network Library is a free open source neural network 
library, which implements multilayer artificial neural networks in C with 
support for both fully connected and sparsely connected networks. 
Cross-platform execution in both fixed and floating point are supported. 
It includes a framework for easy handling of training data sets. It is easy to 
use, versatile, well documented, and fast. Bindings to more than 15 programming
languages are available. An easy to read introduction article and a reference 
manual accompanies the library with examples and recommendations on how to use 
the library. Several graphical user interfaces are also available for the 
library.

%files -n %{fxlibname}
%{_libdir}/libfixedfann.so.%{major}
%{_libdir}/libfixedfann.so.%{major}.*0

%package -n %{fllibname}
Summary: Fast Artificial Neural Network library using floats
Group: System/Libraries

%description -n %{fllibname}
Fast Artificial Neural Network Library is a free open source neural network 
library, which implements multilayer artificial neural networks in C with 
support for both fully connected and sparsely connected networks. 
Cross-platform execution in both fixed and floating point are supported. 
It includes a framework for easy handling of training data sets. It is easy to 
use, versatile, well documented, and fast. Bindings to more than 15 programming
languages are available. An easy to read introduction article and a reference 
manual accompanies the library with examples and recommendations on how to use 
the library. Several graphical user interfaces are also available for the 
library.

%files -n %{fllibname}
%{_libdir}/libfloatfann.so.%{major}
%{_libdir}/libfloatfann.so.%{major}.*0

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: %{dlibname} = %{EVRD}
Requires: %{fllibname} = %{EVRD}
Requires: %{fxlibname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Fast Artificial Neural Network Library is a free open source neural network 
library, which implements multilayer artificial neural networks in C with 
support for both fully connected and sparsely connected networks. 
Cross-platform execution in both fixed and floating point are supported. 
It includes a framework for easy handling of training data sets. It is easy to 
use, versatile, well documented, and fast. Bindings to more than 15 programming
languages are available. An easy to read introduction article and a reference 
manual accompanies the library with examples and recommendations on how to use 
the library. Several graphical user interfaces are also available for the 
library.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%prep
%setup -q
%apply_patches

%if "%{_lib}" != "lib"
sed -i -e 's,lib/pkgconfig,%{_lib}/pkgconfig,g' CMakeLists.txt
%endif

%cmake \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
