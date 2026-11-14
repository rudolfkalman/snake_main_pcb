// Work around the KiCad 10 PROPERTY_ENUM startup assertion dialog deadlock.
// Keep all other assertion dialogs and the original assertion stderr output.
#include <wx/apptrait.h>
#include <wx/string.h>
#include <dlfcn.h>
#include <cstdio>
#include <cstdlib>

bool wxGUIAppTraits::ShowAssertDialog(const wxString& message)
{
    if (message.Contains("property.h")
        && message.Contains("PROPERTY_ENUM")
        && message.Contains("m_choices.GetCount() > 0")
        && message.Contains("No enum choices defined"))
    {
        std::fputs("[KiCad startup workaround] PROPERTY_ENUM warning logged; "
                   "skipping its blocking dialog.\n", stderr);
        // false means do not globally suppress subsequent assertions.
        return false;
    }

    using Original = bool (*)(wxGUIAppTraits*, const wxString&);
    static const auto original = reinterpret_cast<Original>(
        dlsym(RTLD_NEXT, "_ZN14wxGUIAppTraits16ShowAssertDialogERK8wxString"));
    if (!original)
    {
        std::fputs("Cannot find the original wxWidgets assertion handler.\n", stderr);
        std::abort();
    }
    return original(this, message);
}
