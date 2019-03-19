Name:           internal-logdistiller
Version:        1.1
Release:        1%{?dist}
Summary:        LogDistiller is a log files merge and sort tool.
License:        Apache License v2
URL:            http://logdistiller.sourceforge.net/
Source0:        http://data.local/MurexRPMs/archives/logdistiller-%{version}.tar.gz
Requires:       internal-oracle-jdk >= 1.8.131
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot
BuildArch:      noarch

# sysroot's configuration
#------------------------
%define _prefix         /opt/internal/root/opt/logdistiller
%define _exec_prefix    %{_prefix}
%define _libdir         %{_prefix}/lib
%define _docdir         %{_prefix}/docs
#------------------------

%description
LogDistiller is a log files merge and sort tool.
It reads log files, parses them into structured log events 
with attributes, then classify them according rules configured
in an XML file.
Classification results go into reports, published according
to the rules configuration: simply stored in a file, sent by
mail, or even added in a news feed. 

%prep
%setup -qn logdistiller-%{version}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_prefix}
# Clean the source archive
rm -rf src sample rules test logs
mv xdocs/* docs && rm -rf xdocs
mv dtd docs && rm -rf dtd
# Copy the file in the targeted prefix
cp -R . $RPM_BUILD_ROOT/%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)

# Files to include
%{_prefix}/logdistiller.jar
%{_libdir}/logdistiller-1.1.jar
%{_libdir}/activation-1.1.jar
%{_libdir}/bsh-2.0b4.jar
%{_libdir}/commons-io-1.3.2.jar
%{_libdir}/commons-lang-2.3.jar
%{_libdir}/formlayoutmakerx-rc7.jar
%{_libdir}/forms-1.0.7.jar
%{_libdir}/jdom-1.0.jar
%{_libdir}/junit-3.8.1.jar
%{_libdir}/mail-1.4.jar
%{_libdir}/rome-0.8.jar

# Files to exclude
%exclude %{_prefix}/pom.xml
%exclude %{_prefix}/LICENSE.txt
%exclude %{_prefix}/NOTICE.txt

%doc
%{_docdir}/apidocs/allclasses-frame.html
%{_docdir}/apidocs/allclasses-noframe.html
%{_docdir}/apidocs/constant-values.html
%{_docdir}/apidocs/deprecated-list.html
%{_docdir}/apidocs/help-doc.html
%{_docdir}/apidocs/index-all.html
%{_docdir}/apidocs/index.html
%{_docdir}/apidocs/net/sf/logdistiller/Attributes.Extension.html
%{_docdir}/apidocs/net/sf/logdistiller/Attributes.html
%{_docdir}/apidocs/net/sf/logdistiller/Condition.html
%{_docdir}/apidocs/net/sf/logdistiller/FactoryMultiplexer.html
%{_docdir}/apidocs/net/sf/logdistiller/LogDistillation.Category.html
%{_docdir}/apidocs/net/sf/logdistiller/LogDistillation.Group.html
%{_docdir}/apidocs/net/sf/logdistiller/LogDistillation.Plugin.html
%{_docdir}/apidocs/net/sf/logdistiller/LogDistillation.html
%{_docdir}/apidocs/net/sf/logdistiller/LogDistiller.Category.html
%{_docdir}/apidocs/net/sf/logdistiller/LogDistiller.Group.html
%{_docdir}/apidocs/net/sf/logdistiller/LogDistiller.LogType.html
%{_docdir}/apidocs/net/sf/logdistiller/LogDistiller.Output.html
%{_docdir}/apidocs/net/sf/logdistiller/LogDistiller.Plugin.html
%{_docdir}/apidocs/net/sf/logdistiller/LogDistiller.Report.html
%{_docdir}/apidocs/net/sf/logdistiller/LogDistiller.html
%{_docdir}/apidocs/net/sf/logdistiller/LogEvent.Factory.html
%{_docdir}/apidocs/net/sf/logdistiller/LogEvent.html
%{_docdir}/apidocs/net/sf/logdistiller/LogEventTestCase.html
%{_docdir}/apidocs/net/sf/logdistiller/LogType.AttributeInfo.html
%{_docdir}/apidocs/net/sf/logdistiller/LogType.Basic.html
%{_docdir}/apidocs/net/sf/logdistiller/LogType.Description.html
%{_docdir}/apidocs/net/sf/logdistiller/LogType.html
%{_docdir}/apidocs/net/sf/logdistiller/LogTypes.html
%{_docdir}/apidocs/net/sf/logdistiller/Match.Contains.html
%{_docdir}/apidocs/net/sf/logdistiller/Match.EndsWith.html
%{_docdir}/apidocs/net/sf/logdistiller/Match.Equals.html
%{_docdir}/apidocs/net/sf/logdistiller/Match.Regexp.html
%{_docdir}/apidocs/net/sf/logdistiller/Match.StartsWith.html
%{_docdir}/apidocs/net/sf/logdistiller/Match.html
%{_docdir}/apidocs/net/sf/logdistiller/Plugin.html
%{_docdir}/apidocs/net/sf/logdistiller/PluginConfigException.html
%{_docdir}/apidocs/net/sf/logdistiller/Plugins.html
%{_docdir}/apidocs/net/sf/logdistiller/PublishHelper.html
%{_docdir}/apidocs/net/sf/logdistiller/Publisher.PublishException.html
%{_docdir}/apidocs/net/sf/logdistiller/Publisher.html
%{_docdir}/apidocs/net/sf/logdistiller/Publishers.html
%{_docdir}/apidocs/net/sf/logdistiller/ReportFormat.PluginReport.html
%{_docdir}/apidocs/net/sf/logdistiller/ReportFormat.html
%{_docdir}/apidocs/net/sf/logdistiller/ReportFormats.html
%{_docdir}/apidocs/net/sf/logdistiller/ant/AntLogDistillation.html
%{_docdir}/apidocs/net/sf/logdistiller/ant/AntLogEvent.html
%{_docdir}/apidocs/net/sf/logdistiller/ant/AntProperty.html
%{_docdir}/apidocs/net/sf/logdistiller/ant/LogDistillerTask.Compressed.html
%{_docdir}/apidocs/net/sf/logdistiller/ant/LogDistillerTask.html
%{_docdir}/apidocs/net/sf/logdistiller/ant/class-use/AntLogDistillation.html
%{_docdir}/apidocs/net/sf/logdistiller/ant/class-use/AntLogEvent.html
%{_docdir}/apidocs/net/sf/logdistiller/ant/class-use/AntProperty.html
%{_docdir}/apidocs/net/sf/logdistiller/ant/class-use/LogDistillerTask.Compressed.html
%{_docdir}/apidocs/net/sf/logdistiller/ant/class-use/LogDistillerTask.html
%{_docdir}/apidocs/net/sf/logdistiller/ant/package-frame.html
%{_docdir}/apidocs/net/sf/logdistiller/ant/package-summary.html
%{_docdir}/apidocs/net/sf/logdistiller/ant/package-tree.html
%{_docdir}/apidocs/net/sf/logdistiller/ant/package-use.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/Attributes.Extension.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/Attributes.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/Condition.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/FactoryMultiplexer.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogDistillation.Category.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogDistillation.Group.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogDistillation.Plugin.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogDistillation.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogDistiller.Category.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogDistiller.Group.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogDistiller.LogType.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogDistiller.Output.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogDistiller.Plugin.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogDistiller.Report.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogDistiller.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogEvent.Factory.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogEvent.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogEventTestCase.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogType.AttributeInfo.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogType.Basic.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogType.Description.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogType.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/LogTypes.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/Match.Contains.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/Match.EndsWith.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/Match.Equals.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/Match.Regexp.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/Match.StartsWith.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/Match.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/Plugin.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/PluginConfigException.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/Plugins.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/PublishHelper.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/Publisher.PublishException.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/Publisher.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/Publishers.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/ReportFormat.PluginReport.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/ReportFormat.html
%{_docdir}/apidocs/net/sf/logdistiller/class-use/ReportFormats.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/LongProgressBar.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/Main.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/MainPanel.GuiSAXErrorHandler.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/MainPanel.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/NewDialog.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/SimpleContainerLayout.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/SimpleLayoutConstraintsManager.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/SwingAdapter.RunException.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/SwingAdapter.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/XmlFileFilter.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/class-use/LongProgressBar.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/class-use/Main.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/class-use/MainPanel.GuiSAXErrorHandler.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/class-use/MainPanel.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/class-use/NewDialog.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/class-use/SimpleContainerLayout.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/class-use/SimpleLayoutConstraintsManager.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/class-use/SwingAdapter.RunException.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/class-use/SwingAdapter.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/class-use/XmlFileFilter.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/package-frame.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/package-summary.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/package-tree.html
%{_docdir}/apidocs/net/sf/logdistiller/gui/package-use.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/BaseLogTypes.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/JBossLogEvent.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/Log4jXmlLogEvent.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/OracleAlertLogEvent.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/SimpleLineLogEvent.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/SyslogLogEvent.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/WeblogicLogEvent.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/class-use/BaseLogTypes.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/class-use/JBossLogEvent.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/class-use/Log4jXmlLogEvent.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/class-use/OracleAlertLogEvent.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/class-use/SimpleLineLogEvent.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/class-use/SyslogLogEvent.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/class-use/WeblogicLogEvent.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/package-frame.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/package-summary.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/package-tree.html
%{_docdir}/apidocs/net/sf/logdistiller/logtypes/package-use.html
%{_docdir}/apidocs/net/sf/logdistiller/package-frame.html
%{_docdir}/apidocs/net/sf/logdistiller/package-summary.html
%{_docdir}/apidocs/net/sf/logdistiller/package-tree.html
%{_docdir}/apidocs/net/sf/logdistiller/package-use.html
%{_docdir}/apidocs/net/sf/logdistiller/plugins/BasePlugins.html
%{_docdir}/apidocs/net/sf/logdistiller/plugins/FreqPlugin.Freq.html
%{_docdir}/apidocs/net/sf/logdistiller/plugins/FreqPlugin.html
%{_docdir}/apidocs/net/sf/logdistiller/plugins/SamplingPlugin.html
%{_docdir}/apidocs/net/sf/logdistiller/plugins/class-use/BasePlugins.html
%{_docdir}/apidocs/net/sf/logdistiller/plugins/class-use/FreqPlugin.Freq.html
%{_docdir}/apidocs/net/sf/logdistiller/plugins/class-use/FreqPlugin.html
%{_docdir}/apidocs/net/sf/logdistiller/plugins/class-use/SamplingPlugin.html
%{_docdir}/apidocs/net/sf/logdistiller/plugins/package-frame.html
%{_docdir}/apidocs/net/sf/logdistiller/plugins/package-summary.html
%{_docdir}/apidocs/net/sf/logdistiller/plugins/package-tree.html
%{_docdir}/apidocs/net/sf/logdistiller/plugins/package-use.html
%{_docdir}/apidocs/net/sf/logdistiller/publishers/BasePublishers.html
%{_docdir}/apidocs/net/sf/logdistiller/publishers/DelegatePublisher.html
%{_docdir}/apidocs/net/sf/logdistiller/publishers/FeedPublisher.html
%{_docdir}/apidocs/net/sf/logdistiller/publishers/FilePublisher.html
%{_docdir}/apidocs/net/sf/logdistiller/publishers/MailPublisher.html
%{_docdir}/apidocs/net/sf/logdistiller/publishers/class-use/BasePublishers.html
%{_docdir}/apidocs/net/sf/logdistiller/publishers/class-use/DelegatePublisher.html
%{_docdir}/apidocs/net/sf/logdistiller/publishers/class-use/FeedPublisher.html
%{_docdir}/apidocs/net/sf/logdistiller/publishers/class-use/FilePublisher.html
%{_docdir}/apidocs/net/sf/logdistiller/publishers/class-use/MailPublisher.html
%{_docdir}/apidocs/net/sf/logdistiller/publishers/package-frame.html
%{_docdir}/apidocs/net/sf/logdistiller/publishers/package-summary.html
%{_docdir}/apidocs/net/sf/logdistiller/publishers/package-tree.html
%{_docdir}/apidocs/net/sf/logdistiller/publishers/package-use.html
%{_docdir}/apidocs/net/sf/logdistiller/reports/BaseReportFormats.html
%{_docdir}/apidocs/net/sf/logdistiller/reports/TextReport.html
%{_docdir}/apidocs/net/sf/logdistiller/reports/XmlReport.html
%{_docdir}/apidocs/net/sf/logdistiller/reports/class-use/BaseReportFormats.html
%{_docdir}/apidocs/net/sf/logdistiller/reports/class-use/TextReport.html
%{_docdir}/apidocs/net/sf/logdistiller/reports/class-use/XmlReport.html
%{_docdir}/apidocs/net/sf/logdistiller/reports/package-frame.html
%{_docdir}/apidocs/net/sf/logdistiller/reports/package-summary.html
%{_docdir}/apidocs/net/sf/logdistiller/reports/package-tree.html
%{_docdir}/apidocs/net/sf/logdistiller/reports/package-use.html
%{_docdir}/apidocs/net/sf/logdistiller/util/BufferingReader.html
%{_docdir}/apidocs/net/sf/logdistiller/util/ExtensionHelper.html
%{_docdir}/apidocs/net/sf/logdistiller/util/FormatUtil.html
%{_docdir}/apidocs/net/sf/logdistiller/util/PropertiesReplacer.html
%{_docdir}/apidocs/net/sf/logdistiller/util/StringCutter.html
%{_docdir}/apidocs/net/sf/logdistiller/util/UncompressInputStream.html
%{_docdir}/apidocs/net/sf/logdistiller/util/class-use/BufferingReader.html
%{_docdir}/apidocs/net/sf/logdistiller/util/class-use/ExtensionHelper.html
%{_docdir}/apidocs/net/sf/logdistiller/util/class-use/FormatUtil.html
%{_docdir}/apidocs/net/sf/logdistiller/util/class-use/PropertiesReplacer.html
%{_docdir}/apidocs/net/sf/logdistiller/util/class-use/StringCutter.html
%{_docdir}/apidocs/net/sf/logdistiller/util/class-use/UncompressInputStream.html
%{_docdir}/apidocs/net/sf/logdistiller/util/package-frame.html
%{_docdir}/apidocs/net/sf/logdistiller/util/package-summary.html
%{_docdir}/apidocs/net/sf/logdistiller/util/package-tree.html
%{_docdir}/apidocs/net/sf/logdistiller/util/package-use.html
%{_docdir}/apidocs/net/sf/logdistiller/xml/DOMConfigurator.html
%{_docdir}/apidocs/net/sf/logdistiller/xml/DOMUtils.html
%{_docdir}/apidocs/net/sf/logdistiller/xml/LogDistillerEntityResolver.html
%{_docdir}/apidocs/net/sf/logdistiller/xml/SAXErrorHandler.html
%{_docdir}/apidocs/net/sf/logdistiller/xml/class-use/DOMConfigurator.html
%{_docdir}/apidocs/net/sf/logdistiller/xml/class-use/DOMUtils.html
%{_docdir}/apidocs/net/sf/logdistiller/xml/class-use/LogDistillerEntityResolver.html
%{_docdir}/apidocs/net/sf/logdistiller/xml/class-use/SAXErrorHandler.html
%{_docdir}/apidocs/net/sf/logdistiller/xml/package-frame.html
%{_docdir}/apidocs/net/sf/logdistiller/xml/package-summary.html
%{_docdir}/apidocs/net/sf/logdistiller/xml/package-tree.html
%{_docdir}/apidocs/net/sf/logdistiller/xml/package-use.html
%{_docdir}/apidocs/options
%{_docdir}/apidocs/overview-frame.html
%{_docdir}/apidocs/overview-summary.html
%{_docdir}/apidocs/overview-tree.html
%{_docdir}/apidocs/package-list
%{_docdir}/apidocs/packages
%{_docdir}/apidocs/resources/inherit.gif
%{_docdir}/apidocs/serialized-form.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/Attributes.Extension.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/Attributes.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/Condition.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/FactoryMultiplexer.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogDistillation.Category.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogDistillation.Group.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogDistillation.Plugin.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogDistillation.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogDistiller.Category.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogDistiller.Group.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogDistiller.LogType.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogDistiller.Output.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogDistiller.Plugin.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogDistiller.Report.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogDistiller.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogEvent.Factory.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogEvent.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogEventTestCase.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogType.AttributeInfo.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogType.Basic.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogType.Description.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogType.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/LogTypes.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/Match.Contains.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/Match.EndsWith.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/Match.Equals.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/Match.Regexp.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/Match.StartsWith.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/Match.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/Plugin.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/PluginConfigException.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/Plugins.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/PublishHelper.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/Publisher.PublishException.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/Publisher.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/Publishers.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/ReportFormat.PluginReport.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/ReportFormat.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/ReportFormats.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/ant/AntLogDistillation.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/ant/AntLogEvent.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/ant/AntProperty.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/ant/LogDistillerTask.Compressed.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/ant/LogDistillerTask.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/gui/LongProgressBar.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/gui/Main.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/gui/MainPanel.GuiSAXErrorHandler.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/gui/MainPanel.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/gui/NewDialog.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/gui/SimpleContainerLayout.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/gui/SimpleLayoutConstraintsManager.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/gui/SwingAdapter.RunException.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/gui/SwingAdapter.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/gui/XmlFileFilter.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/logtypes/BaseLogTypes.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/logtypes/JBossLogEvent.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/logtypes/Log4jXmlLogEvent.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/logtypes/OracleAlertLogEvent.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/logtypes/SimpleLineLogEvent.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/logtypes/SyslogLogEvent.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/logtypes/WeblogicLogEvent.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/plugins/BasePlugins.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/plugins/FreqPlugin.Freq.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/plugins/FreqPlugin.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/plugins/SamplingPlugin.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/publishers/BasePublishers.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/publishers/DelegatePublisher.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/publishers/FeedPublisher.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/publishers/FilePublisher.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/publishers/MailPublisher.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/reports/BaseReportFormats.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/reports/TextReport.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/reports/XmlReport.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/util/BufferingReader.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/util/ExtensionHelper.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/util/FormatUtil.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/util/PropertiesReplacer.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/util/StringCutter.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/util/UncompressInputStream.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/xml/DOMConfigurator.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/xml/DOMUtils.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/xml/LogDistillerEntityResolver.html
%{_docdir}/apidocs/src-html/net/sf/logdistiller/xml/SAXErrorHandler.html
%{_docdir}/apidocs/stylesheet.css
%{_docdir}/cobertura/css/help.css
%{_docdir}/cobertura/css/main.css
%{_docdir}/cobertura/css/sortabletable.css
%{_docdir}/cobertura/css/source-viewer.css
%{_docdir}/cobertura/css/tooltip.css
%{_docdir}/cobertura/frame-packages.html
%{_docdir}/cobertura/frame-sourcefiles-net.sf.logdistiller.ant.html
%{_docdir}/cobertura/frame-sourcefiles-net.sf.logdistiller.gui.html
%{_docdir}/cobertura/frame-sourcefiles-net.sf.logdistiller.html
%{_docdir}/cobertura/frame-sourcefiles-net.sf.logdistiller.logtypes.html
%{_docdir}/cobertura/frame-sourcefiles-net.sf.logdistiller.plugins.html
%{_docdir}/cobertura/frame-sourcefiles-net.sf.logdistiller.publishers.html
%{_docdir}/cobertura/frame-sourcefiles-net.sf.logdistiller.reports.html
%{_docdir}/cobertura/frame-sourcefiles-net.sf.logdistiller.util.html
%{_docdir}/cobertura/frame-sourcefiles-net.sf.logdistiller.xml.html
%{_docdir}/cobertura/frame-sourcefiles.html
%{_docdir}/cobertura/frame-summary-net.sf.logdistiller.ant.html
%{_docdir}/cobertura/frame-summary-net.sf.logdistiller.gui.html
%{_docdir}/cobertura/frame-summary-net.sf.logdistiller.html
%{_docdir}/cobertura/frame-summary-net.sf.logdistiller.logtypes.html
%{_docdir}/cobertura/frame-summary-net.sf.logdistiller.plugins.html
%{_docdir}/cobertura/frame-summary-net.sf.logdistiller.publishers.html
%{_docdir}/cobertura/frame-summary-net.sf.logdistiller.reports.html
%{_docdir}/cobertura/frame-summary-net.sf.logdistiller.util.html
%{_docdir}/cobertura/frame-summary-net.sf.logdistiller.xml.html
%{_docdir}/cobertura/frame-summary.html
%{_docdir}/cobertura/help.html
%{_docdir}/cobertura/images/blank.png
%{_docdir}/cobertura/images/downsimple.png
%{_docdir}/cobertura/images/upsimple.png
%{_docdir}/cobertura/index.html
%{_docdir}/cobertura/js/customsorttypes.js
%{_docdir}/cobertura/js/popup.js
%{_docdir}/cobertura/js/sortabletable.js
%{_docdir}/cobertura/js/stringbuilder.js
%{_docdir}/cobertura/net.sf.logdistiller.Attributes.html
%{_docdir}/cobertura/net.sf.logdistiller.Condition.html
%{_docdir}/cobertura/net.sf.logdistiller.FactoryMultiplexer.html
%{_docdir}/cobertura/net.sf.logdistiller.LogDistillation.html
%{_docdir}/cobertura/net.sf.logdistiller.LogDistiller.html
%{_docdir}/cobertura/net.sf.logdistiller.LogEvent.html
%{_docdir}/cobertura/net.sf.logdistiller.LogEventTestCase.html
%{_docdir}/cobertura/net.sf.logdistiller.LogType.html
%{_docdir}/cobertura/net.sf.logdistiller.LogTypes.html
%{_docdir}/cobertura/net.sf.logdistiller.Match.html
%{_docdir}/cobertura/net.sf.logdistiller.Plugin.html
%{_docdir}/cobertura/net.sf.logdistiller.PluginConfigException.html
%{_docdir}/cobertura/net.sf.logdistiller.Plugins.html
%{_docdir}/cobertura/net.sf.logdistiller.PublishHelper.html
%{_docdir}/cobertura/net.sf.logdistiller.Publisher.html
%{_docdir}/cobertura/net.sf.logdistiller.Publishers.html
%{_docdir}/cobertura/net.sf.logdistiller.ReportFormat.html
%{_docdir}/cobertura/net.sf.logdistiller.ReportFormats.html
%{_docdir}/cobertura/net.sf.logdistiller.ant.AntLogDistillation.html
%{_docdir}/cobertura/net.sf.logdistiller.ant.AntLogEvent.html
%{_docdir}/cobertura/net.sf.logdistiller.ant.AntProperty.html
%{_docdir}/cobertura/net.sf.logdistiller.ant.LogDistillerTask.html
%{_docdir}/cobertura/net.sf.logdistiller.gui.LongProgressBar.html
%{_docdir}/cobertura/net.sf.logdistiller.gui.Main.html
%{_docdir}/cobertura/net.sf.logdistiller.gui.MainPanel.html
%{_docdir}/cobertura/net.sf.logdistiller.gui.NewDialog.html
%{_docdir}/cobertura/net.sf.logdistiller.gui.SimpleContainerLayout.html
%{_docdir}/cobertura/net.sf.logdistiller.gui.SimpleLayoutConstraintsManager.html
%{_docdir}/cobertura/net.sf.logdistiller.gui.SwingAdapter.html
%{_docdir}/cobertura/net.sf.logdistiller.gui.XmlFileFilter.html
%{_docdir}/cobertura/net.sf.logdistiller.logtypes.BaseLogTypes.html
%{_docdir}/cobertura/net.sf.logdistiller.logtypes.JBossLogEvent.html
%{_docdir}/cobertura/net.sf.logdistiller.logtypes.Log4jXmlLogEvent.html
%{_docdir}/cobertura/net.sf.logdistiller.logtypes.OracleAlertLogEvent.html
%{_docdir}/cobertura/net.sf.logdistiller.logtypes.SimpleLineLogEvent.html
%{_docdir}/cobertura/net.sf.logdistiller.logtypes.SyslogLogEvent.html
%{_docdir}/cobertura/net.sf.logdistiller.logtypes.WeblogicLogEvent.html
%{_docdir}/cobertura/net.sf.logdistiller.plugins.BasePlugins.html
%{_docdir}/cobertura/net.sf.logdistiller.plugins.FreqPlugin.html
%{_docdir}/cobertura/net.sf.logdistiller.plugins.SamplingPlugin.html
%{_docdir}/cobertura/net.sf.logdistiller.publishers.BasePublishers.html
%{_docdir}/cobertura/net.sf.logdistiller.publishers.DelegatePublisher.html
%{_docdir}/cobertura/net.sf.logdistiller.publishers.FeedPublisher.html
%{_docdir}/cobertura/net.sf.logdistiller.publishers.FilePublisher.html
%{_docdir}/cobertura/net.sf.logdistiller.publishers.MailPublisher.html
%{_docdir}/cobertura/net.sf.logdistiller.reports.BaseReportFormats.html
%{_docdir}/cobertura/net.sf.logdistiller.reports.TextReport.html
%{_docdir}/cobertura/net.sf.logdistiller.reports.XmlReport.html
%{_docdir}/cobertura/net.sf.logdistiller.util.BufferingReader.html
%{_docdir}/cobertura/net.sf.logdistiller.util.ExtensionHelper.html
%{_docdir}/cobertura/net.sf.logdistiller.util.FormatUtil.html
%{_docdir}/cobertura/net.sf.logdistiller.util.PropertiesReplacer.html
%{_docdir}/cobertura/net.sf.logdistiller.util.StringCutter.html
%{_docdir}/cobertura/net.sf.logdistiller.util.UncompressInputStream.html
%{_docdir}/cobertura/net.sf.logdistiller.xml.DOMConfigurator.html
%{_docdir}/cobertura/net.sf.logdistiller.xml.DOMUtils.html
%{_docdir}/cobertura/net.sf.logdistiller.xml.LogDistillerEntityResolver.html
%{_docdir}/cobertura/net.sf.logdistiller.xml.SAXErrorHandler.html
%{_docdir}/cpd.html
%{_docdir}/cpd.xml
%{_docdir}/css/maven-base.css
%{_docdir}/css/maven-theme.css
%{_docdir}/css/print.css
%{_docdir}/css/site.css
%{_docdir}/dependencies.html
%{_docdir}/dtddoc/DTDDocStyle.css
%{_docdir}/dtddoc/cctree.js
%{_docdir}/dtddoc/dtreeStyle.css
%{_docdir}/dtddoc/elementsIndex.html
%{_docdir}/dtddoc/img/empty.gif
%{_docdir}/dtddoc/img/join.gif
%{_docdir}/dtddoc/img/joinbottom.gif
%{_docdir}/dtddoc/img/line.gif
%{_docdir}/dtddoc/img/minus.gif
%{_docdir}/dtddoc/img/minusbottom.gif
%{_docdir}/dtddoc/img/plus.gif
%{_docdir}/dtddoc/img/plusbottom.gif
%{_docdir}/dtddoc/index.html
%{_docdir}/dtddoc/intro.html
%{_docdir}/dtddoc/logdistiller-1_4.dtd.html
%{_docdir}/dtddoc/logdistiller-1_4.dtd.org.html
%{_docdir}/dtddoc/toc.html
%{_docdir}/findbugs.html
%{_docdir}/images/close.gif
%{_docdir}/images/collapsed.gif
%{_docdir}/images/expanded.gif
%{_docdir}/images/external.png
%{_docdir}/images/icon_error_sml.gif
%{_docdir}/images/icon_info_sml.gif
%{_docdir}/images/icon_success_sml.gif
%{_docdir}/images/icon_warning_sml.gif
%{_docdir}/images/logos/build-by-maven-black.png
%{_docdir}/images/logos/build-by-maven-white.png
%{_docdir}/images/logos/maven-feather.png
%{_docdir}/images/newwindow.png
%{_docdir}/index.html
%{_docdir}/install.html
%{_docdir}/integration.html
%{_docdir}/issue-tracking.html
%{_docdir}/javancss.html
%{_docdir}/jdepend-report.html
%{_docdir}/license.html
%{_docdir}/logdistiller.html
%{_docdir}/mail-lists.html
%{_docdir}/plugin-management.html
%{_docdir}/plugins.html
%{_docdir}/pmd.html
%{_docdir}/pmd.xml
%{_docdir}/project-info.html
%{_docdir}/project-reports.html
%{_docdir}/project-summary.html
%{_docdir}/quickstart-1.html
%{_docdir}/quickstart-2.html
%{_docdir}/quickstart-3.html
%{_docdir}/quickstart-4.html
%{_docdir}/quickstart-5.html
%{_docdir}/quickstart-6.html
%{_docdir}/quickstart.html
%{_docdir}/screenshot-generated.png
%{_docdir}/screenshot-new.png
%{_docdir}/screenshot-run.png
%{_docdir}/screenshot.png
%{_docdir}/source-repository.html
%{_docdir}/statcvs/author_hboutemy.html
%{_docdir}/statcvs/authors.html
%{_docdir}/statcvs/avgsize.png
%{_docdir}/statcvs/commit_by_day.png
%{_docdir}/statcvs/commit_by_hour.png
%{_docdir}/statcvs/commit_hboutemy_by_day.png
%{_docdir}/statcvs/commit_hboutemy_by_hour.png
%{_docdir}/statcvs/commitactivity_by_author.png
%{_docdir}/statcvs/commitlog.html
%{_docdir}/statcvs/commitlog_1.html
%{_docdir}/statcvs/commitlog_2.html
%{_docdir}/statcvs/commitlog_3.html
%{_docdir}/statcvs/commitlog_4.html
%{_docdir}/statcvs/directory_.html
%{_docdir}/statcvs/directory_sample.html
%{_docdir}/statcvs/directory_sample_src.html
%{_docdir}/statcvs/directory_sample_src_custom.html
%{_docdir}/statcvs/directory_sample_test_custom.html
%{_docdir}/statcvs/directory_src.html
%{_docdir}/statcvs/directory_src_main_assembly.html
%{_docdir}/statcvs/directory_src_main_mdo.html
%{_docdir}/statcvs/directory_src_net_sf_logdistiller.html
%{_docdir}/statcvs/directory_src_net_sf_logdistiller_ant.html
%{_docdir}/statcvs/directory_src_net_sf_logdistiller_gui.html
%{_docdir}/statcvs/directory_src_net_sf_logdistiller_logtypes.html
%{_docdir}/statcvs/directory_src_net_sf_logdistiller_plugins.html
%{_docdir}/statcvs/directory_src_net_sf_logdistiller_publishers.html
%{_docdir}/statcvs/directory_src_net_sf_logdistiller_reports.html
%{_docdir}/statcvs/directory_src_net_sf_logdistiller_util.html
%{_docdir}/statcvs/directory_src_net_sf_logdistiller_xml.html
%{_docdir}/statcvs/directory_src_site.html
%{_docdir}/statcvs/directory_src_site_resources.html
%{_docdir}/statcvs/directory_test.html
%{_docdir}/statcvs/directory_test_net_sf_logdistiller.html
%{_docdir}/statcvs/directory_test_net_sf_logdistiller_ant.html
%{_docdir}/statcvs/directory_test_net_sf_logdistiller_gui.html
%{_docdir}/statcvs/directory_test_net_sf_logdistiller_logtypes.html
%{_docdir}/statcvs/directory_test_net_sf_logdistiller_plugins.html
%{_docdir}/statcvs/directory_test_net_sf_logdistiller_reports.html
%{_docdir}/statcvs/directory_test_net_sf_logdistiller_util.html
%{_docdir}/statcvs/directory_test_net_sf_logdistiller_xml.html
%{_docdir}/statcvs/directory_xdocs.html
%{_docdir}/statcvs/directory_xdocs_style.html
%{_docdir}/statcvs/evolution.html
%{_docdir}/statcvs/evolution.png
%{_docdir}/statcvs/file_count.png
%{_docdir}/statcvs/file_stats.html
%{_docdir}/statcvs/folder-deleted.png
%{_docdir}/statcvs/folder-open.png
%{_docdir}/statcvs/folder.png
%{_docdir}/statcvs/index.html
%{_docdir}/statcvs/loc.png
%{_docdir}/statcvs/loc_.png
%{_docdir}/statcvs/loc_by_module.png
%{_docdir}/statcvs/loc_hboutemy.png
%{_docdir}/statcvs/loc_per_author.png
%{_docdir}/statcvs/loc_sample_.png
%{_docdir}/statcvs/loc_sample_src_.png
%{_docdir}/statcvs/loc_sample_src_custom_.png
%{_docdir}/statcvs/loc_sample_test_custom_.png
%{_docdir}/statcvs/loc_src_.png
%{_docdir}/statcvs/loc_src_main_assembly_.png
%{_docdir}/statcvs/loc_src_main_mdo_.png
%{_docdir}/statcvs/loc_src_net_sf_logdistiller_.png
%{_docdir}/statcvs/loc_src_net_sf_logdistiller_ant_.png
%{_docdir}/statcvs/loc_src_net_sf_logdistiller_gui_.png
%{_docdir}/statcvs/loc_src_net_sf_logdistiller_logtypes_.png
%{_docdir}/statcvs/loc_src_net_sf_logdistiller_plugins_.png
%{_docdir}/statcvs/loc_src_net_sf_logdistiller_publishers_.png
%{_docdir}/statcvs/loc_src_net_sf_logdistiller_reports_.png
%{_docdir}/statcvs/loc_src_net_sf_logdistiller_util_.png
%{_docdir}/statcvs/loc_src_net_sf_logdistiller_xml_.png
%{_docdir}/statcvs/loc_src_site_.png
%{_docdir}/statcvs/loc_src_site_resources_.png
%{_docdir}/statcvs/loc_test_.png
%{_docdir}/statcvs/loc_test_net_sf_logdistiller_.png
%{_docdir}/statcvs/loc_test_net_sf_logdistiller_ant_.png
%{_docdir}/statcvs/loc_test_net_sf_logdistiller_gui_.png
%{_docdir}/statcvs/loc_test_net_sf_logdistiller_logtypes_.png
%{_docdir}/statcvs/loc_test_net_sf_logdistiller_plugins_.png
%{_docdir}/statcvs/loc_test_net_sf_logdistiller_reports_.png
%{_docdir}/statcvs/loc_test_net_sf_logdistiller_util_.png
%{_docdir}/statcvs/loc_test_net_sf_logdistiller_xml_.png
%{_docdir}/statcvs/loc_xdocs_.png
%{_docdir}/statcvs/loc_xdocs_style_.png
%{_docdir}/statcvs/module_stats.html
%{_docdir}/statcvs/progression_by_module.png
%{_docdir}/statcvs/recent_activity.html
%{_docdir}/statcvs/recent_commit_activity.png
%{_docdir}/statcvs/size_by_module.png
%{_docdir}/statcvs/size_hboutemy_by_module.png
%{_docdir}/statcvs/size_per_author.png
%{_docdir}/statcvs/version_stats.html
%{_docdir}/surefire-report.html
%{_docdir}/team-list.html
%{_docdir}/testapidocs/allclasses-frame.html
%{_docdir}/testapidocs/allclasses-noframe.html
%{_docdir}/testapidocs/constant-values.html
%{_docdir}/testapidocs/deprecated-list.html
%{_docdir}/testapidocs/help-doc.html
%{_docdir}/testapidocs/index-all.html
%{_docdir}/testapidocs/index.html
%{_docdir}/testapidocs/net/sf/logdistiller/FactoryMultiplexerTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/LogDistillationTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/TestComparableEvent.Factory.html
%{_docdir}/testapidocs/net/sf/logdistiller/TestComparableEvent.html
%{_docdir}/testapidocs/net/sf/logdistiller/TestEvent.Comparator.html
%{_docdir}/testapidocs/net/sf/logdistiller/TestEvent.Description.html
%{_docdir}/testapidocs/net/sf/logdistiller/TestEvent.Factory.html
%{_docdir}/testapidocs/net/sf/logdistiller/TestEvent.html
%{_docdir}/testapidocs/net/sf/logdistiller/TestLogType.TestDescription.html
%{_docdir}/testapidocs/net/sf/logdistiller/TestLogType.html
%{_docdir}/testapidocs/net/sf/logdistiller/TestLogTypes.html
%{_docdir}/testapidocs/net/sf/logdistiller/TestPlugin.html
%{_docdir}/testapidocs/net/sf/logdistiller/TestPlugins.html
%{_docdir}/testapidocs/net/sf/logdistiller/TestPublisher.html
%{_docdir}/testapidocs/net/sf/logdistiller/TestPublishers.html
%{_docdir}/testapidocs/net/sf/logdistiller/class-use/FactoryMultiplexerTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/class-use/LogDistillationTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/class-use/TestComparableEvent.Factory.html
%{_docdir}/testapidocs/net/sf/logdistiller/class-use/TestComparableEvent.html
%{_docdir}/testapidocs/net/sf/logdistiller/class-use/TestEvent.Comparator.html
%{_docdir}/testapidocs/net/sf/logdistiller/class-use/TestEvent.Description.html
%{_docdir}/testapidocs/net/sf/logdistiller/class-use/TestEvent.Factory.html
%{_docdir}/testapidocs/net/sf/logdistiller/class-use/TestEvent.html
%{_docdir}/testapidocs/net/sf/logdistiller/class-use/TestLogType.TestDescription.html
%{_docdir}/testapidocs/net/sf/logdistiller/class-use/TestLogType.html
%{_docdir}/testapidocs/net/sf/logdistiller/class-use/TestLogTypes.html
%{_docdir}/testapidocs/net/sf/logdistiller/class-use/TestPlugin.html
%{_docdir}/testapidocs/net/sf/logdistiller/class-use/TestPlugins.html
%{_docdir}/testapidocs/net/sf/logdistiller/class-use/TestPublisher.html
%{_docdir}/testapidocs/net/sf/logdistiller/class-use/TestPublishers.html
%{_docdir}/testapidocs/net/sf/logdistiller/gui/MainPanelTest.html
%{_docdir}/testapidocs/net/sf/logdistiller/gui/class-use/MainPanelTest.html
%{_docdir}/testapidocs/net/sf/logdistiller/gui/package-frame.html
%{_docdir}/testapidocs/net/sf/logdistiller/gui/package-summary.html
%{_docdir}/testapidocs/net/sf/logdistiller/gui/package-tree.html
%{_docdir}/testapidocs/net/sf/logdistiller/gui/package-use.html
%{_docdir}/testapidocs/net/sf/logdistiller/logtypes/JBossLogEventTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/logtypes/Log4jXmlLogEventTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/logtypes/OracleAlertLogEventTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/logtypes/SimpleLineLogEventTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/logtypes/SyslogLogEventTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/logtypes/WeblogicLogEventTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/logtypes/class-use/JBossLogEventTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/logtypes/class-use/Log4jXmlLogEventTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/logtypes/class-use/OracleAlertLogEventTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/logtypes/class-use/SimpleLineLogEventTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/logtypes/class-use/SyslogLogEventTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/logtypes/class-use/WeblogicLogEventTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/logtypes/package-frame.html
%{_docdir}/testapidocs/net/sf/logdistiller/logtypes/package-summary.html
%{_docdir}/testapidocs/net/sf/logdistiller/logtypes/package-tree.html
%{_docdir}/testapidocs/net/sf/logdistiller/logtypes/package-use.html
%{_docdir}/testapidocs/net/sf/logdistiller/package-frame.html
%{_docdir}/testapidocs/net/sf/logdistiller/package-summary.html
%{_docdir}/testapidocs/net/sf/logdistiller/package-tree.html
%{_docdir}/testapidocs/net/sf/logdistiller/package-use.html
%{_docdir}/testapidocs/net/sf/logdistiller/plugins/FreqPluginTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/plugins/class-use/FreqPluginTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/plugins/package-frame.html
%{_docdir}/testapidocs/net/sf/logdistiller/plugins/package-summary.html
%{_docdir}/testapidocs/net/sf/logdistiller/plugins/package-tree.html
%{_docdir}/testapidocs/net/sf/logdistiller/plugins/package-use.html
%{_docdir}/testapidocs/net/sf/logdistiller/reports/TextReportTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/reports/XmlReportTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/reports/class-use/TextReportTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/reports/class-use/XmlReportTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/reports/package-frame.html
%{_docdir}/testapidocs/net/sf/logdistiller/reports/package-summary.html
%{_docdir}/testapidocs/net/sf/logdistiller/reports/package-tree.html
%{_docdir}/testapidocs/net/sf/logdistiller/reports/package-use.html
%{_docdir}/testapidocs/net/sf/logdistiller/util/BufferingReaderTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/util/FormatUtilTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/util/PropertiesReplacerTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/util/StringCutterTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/util/class-use/BufferingReaderTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/util/class-use/FormatUtilTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/util/class-use/PropertiesReplacerTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/util/class-use/StringCutterTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/util/package-frame.html
%{_docdir}/testapidocs/net/sf/logdistiller/util/package-summary.html
%{_docdir}/testapidocs/net/sf/logdistiller/util/package-tree.html
%{_docdir}/testapidocs/net/sf/logdistiller/util/package-use.html
%{_docdir}/testapidocs/net/sf/logdistiller/xml/DOMConfiguratorTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/xml/class-use/DOMConfiguratorTestCase.html
%{_docdir}/testapidocs/net/sf/logdistiller/xml/package-frame.html
%{_docdir}/testapidocs/net/sf/logdistiller/xml/package-summary.html
%{_docdir}/testapidocs/net/sf/logdistiller/xml/package-tree.html
%{_docdir}/testapidocs/net/sf/logdistiller/xml/package-use.html
%{_docdir}/testapidocs/options
%{_docdir}/testapidocs/overview-frame.html
%{_docdir}/testapidocs/overview-summary.html
%{_docdir}/testapidocs/overview-tree.html
%{_docdir}/testapidocs/package-list
%{_docdir}/testapidocs/packages
%{_docdir}/testapidocs/resources/inherit.gif
%{_docdir}/testapidocs/serialized-form.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/FactoryMultiplexerTestCase.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/LogDistillationTestCase.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/TestComparableEvent.Factory.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/TestComparableEvent.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/TestEvent.Comparator.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/TestEvent.Description.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/TestEvent.Factory.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/TestEvent.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/TestLogType.TestDescription.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/TestLogType.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/TestLogTypes.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/TestPlugin.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/TestPlugins.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/TestPublisher.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/TestPublishers.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/gui/MainPanelTest.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/logtypes/JBossLogEventTestCase.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/logtypes/Log4jXmlLogEventTestCase.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/logtypes/OracleAlertLogEventTestCase.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/logtypes/SimpleLineLogEventTestCase.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/logtypes/SyslogLogEventTestCase.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/logtypes/WeblogicLogEventTestCase.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/plugins/FreqPluginTestCase.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/reports/TextReportTestCase.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/reports/XmlReportTestCase.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/util/BufferingReaderTestCase.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/util/FormatUtilTestCase.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/util/PropertiesReplacerTestCase.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/util/StringCutterTestCase.html
%{_docdir}/testapidocs/src-html/net/sf/logdistiller/xml/DOMConfiguratorTestCase.html
%{_docdir}/testapidocs/stylesheet.css
%{_docdir}/todo.html
%{_docdir}/upgrade.html
%{_docdir}/xref-test/allclasses-frame.html
%{_docdir}/xref-test/index.html
%{_docdir}/xref-test/net/sf/logdistiller/FactoryMultiplexerTestCase.html
%{_docdir}/xref-test/net/sf/logdistiller/LogDistillationTestCase.html
%{_docdir}/xref-test/net/sf/logdistiller/TestComparableEvent.html
%{_docdir}/xref-test/net/sf/logdistiller/TestEvent.html
%{_docdir}/xref-test/net/sf/logdistiller/TestLogType.html
%{_docdir}/xref-test/net/sf/logdistiller/TestLogTypes.html
%{_docdir}/xref-test/net/sf/logdistiller/TestPlugin.html
%{_docdir}/xref-test/net/sf/logdistiller/TestPlugins.html
%{_docdir}/xref-test/net/sf/logdistiller/TestPublisher.html
%{_docdir}/xref-test/net/sf/logdistiller/TestPublishers.html
%{_docdir}/xref-test/net/sf/logdistiller/gui/MainPanelTest.html
%{_docdir}/xref-test/net/sf/logdistiller/gui/package-frame.html
%{_docdir}/xref-test/net/sf/logdistiller/gui/package-summary.html
%{_docdir}/xref-test/net/sf/logdistiller/logtypes/JBossLogEventTestCase.html
%{_docdir}/xref-test/net/sf/logdistiller/logtypes/Log4jXmlLogEventTestCase.html
%{_docdir}/xref-test/net/sf/logdistiller/logtypes/OracleAlertLogEventTestCase.html
%{_docdir}/xref-test/net/sf/logdistiller/logtypes/SimpleLineLogEventTestCase.html
%{_docdir}/xref-test/net/sf/logdistiller/logtypes/SyslogLogEventTestCase.html
%{_docdir}/xref-test/net/sf/logdistiller/logtypes/WeblogicLogEventTestCase.html
%{_docdir}/xref-test/net/sf/logdistiller/logtypes/package-frame.html
%{_docdir}/xref-test/net/sf/logdistiller/logtypes/package-summary.html
%{_docdir}/xref-test/net/sf/logdistiller/package-frame.html
%{_docdir}/xref-test/net/sf/logdistiller/package-summary.html
%{_docdir}/xref-test/net/sf/logdistiller/plugins/FreqPluginTestCase.html
%{_docdir}/xref-test/net/sf/logdistiller/plugins/package-frame.html
%{_docdir}/xref-test/net/sf/logdistiller/plugins/package-summary.html
%{_docdir}/xref-test/net/sf/logdistiller/reports/TextReportTestCase.html
%{_docdir}/xref-test/net/sf/logdistiller/reports/XmlReportTestCase.html
%{_docdir}/xref-test/net/sf/logdistiller/reports/package-frame.html
%{_docdir}/xref-test/net/sf/logdistiller/reports/package-summary.html
%{_docdir}/xref-test/net/sf/logdistiller/util/BufferingReaderTestCase.html
%{_docdir}/xref-test/net/sf/logdistiller/util/FormatUtilTestCase.html
%{_docdir}/xref-test/net/sf/logdistiller/util/PropertiesReplacerTestCase.html
%{_docdir}/xref-test/net/sf/logdistiller/util/StringCutterTestCase.html
%{_docdir}/xref-test/net/sf/logdistiller/util/package-frame.html
%{_docdir}/xref-test/net/sf/logdistiller/util/package-summary.html
%{_docdir}/xref-test/net/sf/logdistiller/xml/DOMConfiguratorTestCase.html
%{_docdir}/xref-test/net/sf/logdistiller/xml/package-frame.html
%{_docdir}/xref-test/net/sf/logdistiller/xml/package-summary.html
%{_docdir}/xref-test/overview-frame.html
%{_docdir}/xref-test/overview-summary.html
%{_docdir}/xref-test/stylesheet.css
%{_docdir}/xref/allclasses-frame.html
%{_docdir}/xref/index.html
%{_docdir}/xref/net/sf/logdistiller/Attributes.html
%{_docdir}/xref/net/sf/logdistiller/Condition.html
%{_docdir}/xref/net/sf/logdistiller/FactoryMultiplexer.html
%{_docdir}/xref/net/sf/logdistiller/LogDistillation.html
%{_docdir}/xref/net/sf/logdistiller/LogDistiller.html
%{_docdir}/xref/net/sf/logdistiller/LogEvent.html
%{_docdir}/xref/net/sf/logdistiller/LogEventTestCase.html
%{_docdir}/xref/net/sf/logdistiller/LogType.html
%{_docdir}/xref/net/sf/logdistiller/LogTypes.html
%{_docdir}/xref/net/sf/logdistiller/Match.html
%{_docdir}/xref/net/sf/logdistiller/Plugin.html
%{_docdir}/xref/net/sf/logdistiller/PluginConfigException.html
%{_docdir}/xref/net/sf/logdistiller/Plugins.html
%{_docdir}/xref/net/sf/logdistiller/PublishHelper.html
%{_docdir}/xref/net/sf/logdistiller/Publisher.html
%{_docdir}/xref/net/sf/logdistiller/Publishers.html
%{_docdir}/xref/net/sf/logdistiller/ReportFormat.html
%{_docdir}/xref/net/sf/logdistiller/ReportFormats.html
%{_docdir}/xref/net/sf/logdistiller/ant/AntLogDistillation.html
%{_docdir}/xref/net/sf/logdistiller/ant/AntLogEvent.html
%{_docdir}/xref/net/sf/logdistiller/ant/AntProperty.html
%{_docdir}/xref/net/sf/logdistiller/ant/LogDistillerTask.html
%{_docdir}/xref/net/sf/logdistiller/ant/package-frame.html
%{_docdir}/xref/net/sf/logdistiller/ant/package-summary.html
%{_docdir}/xref/net/sf/logdistiller/gui/LongProgressBar.html
%{_docdir}/xref/net/sf/logdistiller/gui/Main.html
%{_docdir}/xref/net/sf/logdistiller/gui/MainPanel.html
%{_docdir}/xref/net/sf/logdistiller/gui/NewDialog.html
%{_docdir}/xref/net/sf/logdistiller/gui/SimpleContainerLayout.html
%{_docdir}/xref/net/sf/logdistiller/gui/SimpleLayoutConstraintsManager.html
%{_docdir}/xref/net/sf/logdistiller/gui/SwingAdapter.html
%{_docdir}/xref/net/sf/logdistiller/gui/XmlFileFilter.html
%{_docdir}/xref/net/sf/logdistiller/gui/package-frame.html
%{_docdir}/xref/net/sf/logdistiller/gui/package-summary.html
%{_docdir}/xref/net/sf/logdistiller/logtypes/BaseLogTypes.html
%{_docdir}/xref/net/sf/logdistiller/logtypes/JBossLogEvent.html
%{_docdir}/xref/net/sf/logdistiller/logtypes/Log4jXmlLogEvent.html
%{_docdir}/xref/net/sf/logdistiller/logtypes/OracleAlertLogEvent.html
%{_docdir}/xref/net/sf/logdistiller/logtypes/SimpleLineLogEvent.html
%{_docdir}/xref/net/sf/logdistiller/logtypes/SyslogLogEvent.html
%{_docdir}/xref/net/sf/logdistiller/logtypes/WeblogicLogEvent.html
%{_docdir}/xref/net/sf/logdistiller/logtypes/package-frame.html
%{_docdir}/xref/net/sf/logdistiller/logtypes/package-summary.html
%{_docdir}/xref/net/sf/logdistiller/package-frame.html
%{_docdir}/xref/net/sf/logdistiller/package-summary.html
%{_docdir}/xref/net/sf/logdistiller/plugins/BasePlugins.html
%{_docdir}/xref/net/sf/logdistiller/plugins/FreqPlugin.html
%{_docdir}/xref/net/sf/logdistiller/plugins/SamplingPlugin.html
%{_docdir}/xref/net/sf/logdistiller/plugins/package-frame.html
%{_docdir}/xref/net/sf/logdistiller/plugins/package-summary.html
%{_docdir}/xref/net/sf/logdistiller/publishers/BasePublishers.html
%{_docdir}/xref/net/sf/logdistiller/publishers/DelegatePublisher.html
%{_docdir}/xref/net/sf/logdistiller/publishers/FeedPublisher.html
%{_docdir}/xref/net/sf/logdistiller/publishers/FilePublisher.html
%{_docdir}/xref/net/sf/logdistiller/publishers/MailPublisher.html
%{_docdir}/xref/net/sf/logdistiller/publishers/package-frame.html
%{_docdir}/xref/net/sf/logdistiller/publishers/package-summary.html
%{_docdir}/xref/net/sf/logdistiller/reports/BaseReportFormats.html
%{_docdir}/xref/net/sf/logdistiller/reports/TextReport.html
%{_docdir}/xref/net/sf/logdistiller/reports/XmlReport.html
%{_docdir}/xref/net/sf/logdistiller/reports/package-frame.html
%{_docdir}/xref/net/sf/logdistiller/reports/package-summary.html
%{_docdir}/xref/net/sf/logdistiller/util/BufferingReader.html
%{_docdir}/xref/net/sf/logdistiller/util/ExtensionHelper.html
%{_docdir}/xref/net/sf/logdistiller/util/FormatUtil.html
%{_docdir}/xref/net/sf/logdistiller/util/PropertiesReplacer.html
%{_docdir}/xref/net/sf/logdistiller/util/StringCutter.html
%{_docdir}/xref/net/sf/logdistiller/util/UncompressInputStream.html
%{_docdir}/xref/net/sf/logdistiller/util/package-frame.html
%{_docdir}/xref/net/sf/logdistiller/util/package-summary.html
%{_docdir}/xref/net/sf/logdistiller/xml/DOMConfigurator.html
%{_docdir}/xref/net/sf/logdistiller/xml/DOMUtils.html
%{_docdir}/xref/net/sf/logdistiller/xml/LogDistillerEntityResolver.html
%{_docdir}/xref/net/sf/logdistiller/xml/SAXErrorHandler.html
%{_docdir}/xref/net/sf/logdistiller/xml/package-frame.html
%{_docdir}/xref/net/sf/logdistiller/xml/package-summary.html
%{_docdir}/xref/overview-frame.html
%{_docdir}/xref/overview-summary.html
%{_docdir}/xref/stylesheet.css
%{_docdir}/xsd/logdistiller-1.1.0.xsd
%{_docdir}/dtd/logdistiller-1_0.dtd
%{_docdir}/dtd/logdistiller-1_1.dtd
%{_docdir}/dtd/logdistiller-1_2.dtd
%{_docdir}/dtd/logdistiller-1_3.dtd
%{_docdir}/dtd/logdistiller-1_4.dtd
%{_docdir}/index.xml
%{_docdir}/install.xml
%{_docdir}/quickstart-1.xml
%{_docdir}/quickstart-2.xml
%{_docdir}/quickstart-3.xml
%{_docdir}/quickstart-4.xml
%{_docdir}/quickstart-5.xml
%{_docdir}/quickstart-6.xml
%{_docdir}/quickstart.xml
%{_docdir}/style/DTDDocStyle.css
%{_docdir}/style/stylesheet.css
%{_docdir}/todo.xml
%{_docdir}/upgrade.xml

# Directories owned by this RPM
%dir %{_prefix}/
%dir %{_libdir}/
%dir %{_docdir}/
%dir %{_docdir}/style
%dir %{_docdir}/css
%dir %{_docdir}/dtd
%dir %{_docdir}/xsd
%dir %{_docdir}/statcvs
%dir %{_docdir}/xref/
%dir %{_docdir}/xref/net/
%dir %{_docdir}/xref/net/sf/
%dir %{_docdir}/xref/net/sf/logdistiller/
%dir %{_docdir}/xref/net/sf/logdistiller/util/
%dir %{_docdir}/xref/net/sf/logdistiller/gui/
%dir %{_docdir}/xref/net/sf/logdistiller/plugins/
%dir %{_docdir}/xref/net/sf/logdistiller/ant/
%dir %{_docdir}/xref/net/sf/logdistiller/publishers/
%dir %{_docdir}/xref/net/sf/logdistiller/xml/
%dir %{_docdir}/xref/net/sf/logdistiller/reports/
%dir %{_docdir}/xref/net/sf/logdistiller/logtypes/
%dir %{_docdir}/dtddoc/
%dir %{_docdir}/dtddoc/img/
%dir %{_docdir}/images/
%dir %{_docdir}/images/logos/
%dir %{_docdir}/cobertura/
%dir %{_docdir}/cobertura/css/
%dir %{_docdir}/cobertura/images/
%dir %{_docdir}/cobertura/js/
%dir %{_docdir}/apidocs/
%dir %{_docdir}/apidocs/net/
%dir %{_docdir}/apidocs/net/sf/
%dir %{_docdir}/apidocs/net/sf/logdistiller/
%dir %{_docdir}/apidocs/net/sf/logdistiller/util/
%dir %{_docdir}/apidocs/net/sf/logdistiller/util/class-use/
%dir %{_docdir}/apidocs/net/sf/logdistiller/gui/
%dir %{_docdir}/apidocs/net/sf/logdistiller/gui/class-use/
%dir %{_docdir}/apidocs/net/sf/logdistiller/plugins/
%dir %{_docdir}/apidocs/net/sf/logdistiller/plugins/class-use/
%dir %{_docdir}/apidocs/net/sf/logdistiller/ant/
%dir %{_docdir}/apidocs/net/sf/logdistiller/ant/class-use/
%dir %{_docdir}/apidocs/net/sf/logdistiller/class-use/
%dir %{_docdir}/apidocs/net/sf/logdistiller/publishers/
%dir %{_docdir}/apidocs/net/sf/logdistiller/publishers/class-use/
%dir %{_docdir}/apidocs/net/sf/logdistiller/xml/
%dir %{_docdir}/apidocs/net/sf/logdistiller/xml/class-use/
%dir %{_docdir}/apidocs/net/sf/logdistiller/reports/
%dir %{_docdir}/apidocs/net/sf/logdistiller/reports/class-use/
%dir %{_docdir}/apidocs/net/sf/logdistiller/logtypes/
%dir %{_docdir}/apidocs/net/sf/logdistiller/logtypes/class-use/
%dir %{_docdir}/apidocs/src-html/
%dir %{_docdir}/apidocs/src-html/net/
%dir %{_docdir}/apidocs/src-html/net/sf/
%dir %{_docdir}/apidocs/src-html/net/sf/logdistiller/
%dir %{_docdir}/apidocs/src-html/net/sf/logdistiller/util/
%dir %{_docdir}/apidocs/src-html/net/sf/logdistiller/gui/
%dir %{_docdir}/apidocs/src-html/net/sf/logdistiller/plugins/
%dir %{_docdir}/apidocs/src-html/net/sf/logdistiller/ant/
%dir %{_docdir}/apidocs/src-html/net/sf/logdistiller/publishers/
%dir %{_docdir}/apidocs/src-html/net/sf/logdistiller/xml/
%dir %{_docdir}/apidocs/src-html/net/sf/logdistiller/reports/
%dir %{_docdir}/apidocs/src-html/net/sf/logdistiller/logtypes/
%dir %{_docdir}/apidocs/resources/
%dir %{_docdir}/xref-test/
%dir %{_docdir}/xref-test/net/
%dir %{_docdir}/xref-test/net/sf/
%dir %{_docdir}/xref-test/net/sf/logdistiller/
%dir %{_docdir}/xref-test/net/sf/logdistiller/util/
%dir %{_docdir}/xref-test/net/sf/logdistiller/gui/
%dir %{_docdir}/xref-test/net/sf/logdistiller/plugins/
%dir %{_docdir}/xref-test/net/sf/logdistiller/xml/
%dir %{_docdir}/xref-test/net/sf/logdistiller/reports/
%dir %{_docdir}/xref-test/net/sf/logdistiller/logtypes/
%dir %{_docdir}/testapidocs/
%dir %{_docdir}/testapidocs/net/
%dir %{_docdir}/testapidocs/net/sf/
%dir %{_docdir}/testapidocs/net/sf/logdistiller/
%dir %{_docdir}/testapidocs/net/sf/logdistiller/util/
%dir %{_docdir}/testapidocs/net/sf/logdistiller/util/class-use/
%dir %{_docdir}/testapidocs/net/sf/logdistiller/gui/
%dir %{_docdir}/testapidocs/net/sf/logdistiller/gui/class-use/
%dir %{_docdir}/testapidocs/net/sf/logdistiller/plugins/
%dir %{_docdir}/testapidocs/net/sf/logdistiller/plugins/class-use/
%dir %{_docdir}/testapidocs/net/sf/logdistiller/class-use/
%dir %{_docdir}/testapidocs/net/sf/logdistiller/xml/
%dir %{_docdir}/testapidocs/net/sf/logdistiller/xml/class-use/
%dir %{_docdir}/testapidocs/net/sf/logdistiller/reports/
%dir %{_docdir}/testapidocs/net/sf/logdistiller/reports/class-use/
%dir %{_docdir}/testapidocs/net/sf/logdistiller/logtypes/
%dir %{_docdir}/testapidocs/net/sf/logdistiller/logtypes/class-use/
%dir %{_docdir}/testapidocs/src-html/
%dir %{_docdir}/testapidocs/src-html/net/
%dir %{_docdir}/testapidocs/src-html/net/sf/
%dir %{_docdir}/testapidocs/src-html/net/sf/logdistiller/
%dir %{_docdir}/testapidocs/src-html/net/sf/logdistiller/util/
%dir %{_docdir}/testapidocs/src-html/net/sf/logdistiller/gui/
%dir %{_docdir}/testapidocs/src-html/net/sf/logdistiller/plugins/
%dir %{_docdir}/testapidocs/src-html/net/sf/logdistiller/xml/
%dir %{_docdir}/testapidocs/src-html/net/sf/logdistiller/reports/
%dir %{_docdir}/testapidocs/src-html/net/sf/logdistiller/logtypes/
%dir %{_docdir}/testapidocs/resources/

%changelog
* Thu Jan 17 2019 Antoine Allard <antoine.allard@internal.com>
- Create the RPM
