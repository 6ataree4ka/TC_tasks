using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using TestStack.White.UIItems.MenuItems;

namespace Paint.Framework.WhiteExtensions
{
    public static class MenuExtensions
    {
        public static void ClickWithLogs(this Menu menu)
        {
            Logger.Log.Info($"Menu '{menu.Name}' opened.");
            menu.Click();
        }
    }
}
