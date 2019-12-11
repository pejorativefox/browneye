Name:       mozjs
Version:    52.2.1
Release:    1
Summary:    TODO
License:    GPL3
Prefix:     /usr
Source0:    %{name}-%{version}gnome1.tar.gz


%description
TODO

%prep
%setup -n mozjs-52.2.1gnome1

%build
pushd js/src
%configure  --with-intl-api     \
            --with-system-zlib  \
            --with-system-nspr  \
            --with-system-icu   \
            --enable-threadsafe \
            --enable-readline
%make_build
popd

%install    
rm -rf %{buildroot}
pushd js/src
%make_install
popd
rm -vf %{buildroot}%{_infodir}/dir*

%files
/usr/bin/js52
/usr/bin/js52-config
/usr/include/mozjs-52/fdlibm.h
/usr/include/mozjs-52/jemalloc_types.h
/usr/include/mozjs-52/js-config.h
/usr/include/mozjs-52/js.msg
/usr/include/mozjs-52/js/CallArgs.h
/usr/include/mozjs-52/js/CallNonGenericMethod.h
/usr/include/mozjs-52/js/CharacterEncoding.h
/usr/include/mozjs-52/js/Class.h
/usr/include/mozjs-52/js/Conversions.h
/usr/include/mozjs-52/js/Date.h
/usr/include/mozjs-52/js/Debug.h
/usr/include/mozjs-52/js/GCAPI.h
/usr/include/mozjs-52/js/GCAnnotations.h
/usr/include/mozjs-52/js/GCHashTable.h
/usr/include/mozjs-52/js/GCPolicyAPI.h
/usr/include/mozjs-52/js/GCVariant.h
/usr/include/mozjs-52/js/GCVector.h
/usr/include/mozjs-52/js/HashTable.h
/usr/include/mozjs-52/js/HeapAPI.h
/usr/include/mozjs-52/js/Id.h
/usr/include/mozjs-52/js/Initialization.h
/usr/include/mozjs-52/js/LegacyIntTypes.h
/usr/include/mozjs-52/js/MemoryMetrics.h
/usr/include/mozjs-52/js/Principals.h
/usr/include/mozjs-52/js/ProfilingFrameIterator.h
/usr/include/mozjs-52/js/ProfilingStack.h
/usr/include/mozjs-52/js/Proxy.h
/usr/include/mozjs-52/js/Realm.h
/usr/include/mozjs-52/js/RequiredDefines.h
/usr/include/mozjs-52/js/RootingAPI.h
/usr/include/mozjs-52/js/SliceBudget.h
/usr/include/mozjs-52/js/StructuredClone.h
/usr/include/mozjs-52/js/SweepingAPI.h
/usr/include/mozjs-52/js/TraceKind.h
/usr/include/mozjs-52/js/TracingAPI.h
/usr/include/mozjs-52/js/TrackedOptimizationInfo.h
/usr/include/mozjs-52/js/TypeDecls.h
/usr/include/mozjs-52/js/UbiNode.h
/usr/include/mozjs-52/js/UbiNodeBreadthFirst.h
/usr/include/mozjs-52/js/UbiNodeCensus.h
/usr/include/mozjs-52/js/UbiNodeDominatorTree.h
/usr/include/mozjs-52/js/UbiNodePostOrder.h
/usr/include/mozjs-52/js/UbiNodeShortestPaths.h
/usr/include/mozjs-52/js/UniquePtr.h
/usr/include/mozjs-52/js/Utility.h
/usr/include/mozjs-52/js/Value.h
/usr/include/mozjs-52/js/Vector.h
/usr/include/mozjs-52/js/WeakMapPtr.h
/usr/include/mozjs-52/jsalloc.h
/usr/include/mozjs-52/jsapi.h
/usr/include/mozjs-52/jsbytecode.h
/usr/include/mozjs-52/jsclist.h
/usr/include/mozjs-52/jscpucfg.h
/usr/include/mozjs-52/jsfriendapi.h
/usr/include/mozjs-52/jsperf.h
/usr/include/mozjs-52/jsprf.h
/usr/include/mozjs-52/jsprototypes.h
/usr/include/mozjs-52/jspubtd.h
/usr/include/mozjs-52/jstypes.h
/usr/include/mozjs-52/jsversion.h
/usr/include/mozjs-52/jswrapper.h
/usr/include/mozjs-52/mozilla/Alignment.h
/usr/include/mozjs-52/mozilla/AllocPolicy.h
/usr/include/mozjs-52/mozilla/AlreadyAddRefed.h
/usr/include/mozjs-52/mozilla/Array.h
/usr/include/mozjs-52/mozilla/ArrayUtils.h
/usr/include/mozjs-52/mozilla/Assertions.h
/usr/include/mozjs-52/mozilla/Atomics.h
/usr/include/mozjs-52/mozilla/Attributes.h
/usr/include/mozjs-52/mozilla/BinarySearch.h
/usr/include/mozjs-52/mozilla/BloomFilter.h
/usr/include/mozjs-52/mozilla/BufferList.h
/usr/include/mozjs-52/mozilla/Casting.h
/usr/include/mozjs-52/mozilla/ChaosMode.h
/usr/include/mozjs-52/mozilla/Char16.h
/usr/include/mozjs-52/mozilla/CheckedInt.h
/usr/include/mozjs-52/mozilla/Compiler.h
/usr/include/mozjs-52/mozilla/Compression.h
/usr/include/mozjs-52/mozilla/DebugOnly.h
/usr/include/mozjs-52/mozilla/Decimal.h
/usr/include/mozjs-52/mozilla/EndianUtils.h
/usr/include/mozjs-52/mozilla/EnumSet.h
/usr/include/mozjs-52/mozilla/EnumTypeTraits.h
/usr/include/mozjs-52/mozilla/EnumeratedArray.h
/usr/include/mozjs-52/mozilla/EnumeratedRange.h
/usr/include/mozjs-52/mozilla/FastBernoulliTrial.h
/usr/include/mozjs-52/mozilla/FloatingPoint.h
/usr/include/mozjs-52/mozilla/Function.h
/usr/include/mozjs-52/mozilla/GuardObjects.h
/usr/include/mozjs-52/mozilla/HashFunctions.h
/usr/include/mozjs-52/mozilla/IndexSequence.h
/usr/include/mozjs-52/mozilla/IntegerPrintfMacros.h
/usr/include/mozjs-52/mozilla/IntegerRange.h
/usr/include/mozjs-52/mozilla/IntegerTypeTraits.h
/usr/include/mozjs-52/mozilla/JSONWriter.h
/usr/include/mozjs-52/mozilla/Likely.h
/usr/include/mozjs-52/mozilla/LinkedList.h
/usr/include/mozjs-52/mozilla/LinuxSignal.h
/usr/include/mozjs-52/mozilla/MacroArgs.h
/usr/include/mozjs-52/mozilla/MacroForEach.h
/usr/include/mozjs-52/mozilla/MathAlgorithms.h
/usr/include/mozjs-52/mozilla/Maybe.h
/usr/include/mozjs-52/mozilla/MaybeOneOf.h
/usr/include/mozjs-52/mozilla/MemoryChecking.h
/usr/include/mozjs-52/mozilla/MemoryReporting.h
/usr/include/mozjs-52/mozilla/Move.h
/usr/include/mozjs-52/mozilla/NotNull.h
/usr/include/mozjs-52/mozilla/NullPtr.h
/usr/include/mozjs-52/mozilla/Opaque.h
/usr/include/mozjs-52/mozilla/OperatorNewExtensions.h
/usr/include/mozjs-52/mozilla/Pair.h
/usr/include/mozjs-52/mozilla/PodOperations.h
/usr/include/mozjs-52/mozilla/Poison.h
/usr/include/mozjs-52/mozilla/Range.h
/usr/include/mozjs-52/mozilla/RangedArray.h
/usr/include/mozjs-52/mozilla/RangedPtr.h
/usr/include/mozjs-52/mozilla/ReentrancyGuard.h
/usr/include/mozjs-52/mozilla/RefCountType.h
/usr/include/mozjs-52/mozilla/RefCounted.h
/usr/include/mozjs-52/mozilla/RefPtr.h
/usr/include/mozjs-52/mozilla/ReverseIterator.h
/usr/include/mozjs-52/mozilla/RollingMean.h
/usr/include/mozjs-52/mozilla/SHA1.h
/usr/include/mozjs-52/mozilla/Saturate.h
/usr/include/mozjs-52/mozilla/ScopeExit.h
/usr/include/mozjs-52/mozilla/Scoped.h
/usr/include/mozjs-52/mozilla/SegmentedVector.h
/usr/include/mozjs-52/mozilla/SizePrintfMacros.h
/usr/include/mozjs-52/mozilla/SplayTree.h
/usr/include/mozjs-52/mozilla/Sprintf.h
/usr/include/mozjs-52/mozilla/StackWalk.h
/usr/include/mozjs-52/mozilla/StaticAnalysisFunctions.h
/usr/include/mozjs-52/mozilla/TaggedAnonymousMemory.h
/usr/include/mozjs-52/mozilla/TemplateLib.h
/usr/include/mozjs-52/mozilla/ThreadLocal.h
/usr/include/mozjs-52/mozilla/TimeStamp.h
/usr/include/mozjs-52/mozilla/ToString.h
/usr/include/mozjs-52/mozilla/Tuple.h
/usr/include/mozjs-52/mozilla/TypeTraits.h
/usr/include/mozjs-52/mozilla/TypedEnumBits.h
/usr/include/mozjs-52/mozilla/Types.h
/usr/include/mozjs-52/mozilla/UniquePtr.h
/usr/include/mozjs-52/mozilla/UniquePtrExtensions.h
/usr/include/mozjs-52/mozilla/Unused.h
/usr/include/mozjs-52/mozilla/Variant.h
/usr/include/mozjs-52/mozilla/Vector.h
/usr/include/mozjs-52/mozilla/WeakPtr.h
/usr/include/mozjs-52/mozilla/XorShift128PlusRNG.h
/usr/include/mozjs-52/mozilla/double-conversion.h
/usr/include/mozjs-52/mozilla/fallible.h
/usr/include/mozjs-52/mozilla/mozalloc.h
/usr/include/mozjs-52/mozilla/mozalloc_abort.h
/usr/include/mozjs-52/mozilla/mozalloc_oom.h
/usr/include/mozjs-52/mozilla/utils.h
/usr/include/mozjs-52/mozmemory.h
/usr/include/mozjs-52/mozmemory_wrap.h
/usr/lib64/libjs_static.ajs
/usr/lib64/libmozjs-52.so
/usr/lib64/pkgconfig/mozjs-52.pc


%changelog
# let's skip this for now

