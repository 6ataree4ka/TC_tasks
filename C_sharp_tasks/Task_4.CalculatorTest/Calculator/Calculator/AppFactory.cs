using System.Configuration;
using TestStack.White;

namespace Calculator
{
    public class AppFactory
    {
        private static AppFactory _instance;
        private Application _application;
        private readonly string _pathToApp;
        
        private AppFactory()
        {
            Logger.InitLogger();
            Logger.Log.Info("========== TEST RUN ==========");
            _pathToApp = ReadConfigParam("pathToApp");
        }

        public static AppFactory Instance
        {
            get
            {
                if (_instance == null)
                {
                    _instance = new AppFactory();
                }
                return _instance;
            }
        }

        public Application LaunchApplication()
        {
            if (_application == null)
            {
                _application = Application.Launch(_pathToApp);
            }
            return _application;
        }

        public void CloseApplication()
        {
            _application.Close();
            _application.Dispose();
            _application = null;

            _instance = null;
        }

        public string ReadConfigParam(string paramName)
        {
            return ConfigurationManager.AppSettings.Get(paramName);
        }
    }
}
