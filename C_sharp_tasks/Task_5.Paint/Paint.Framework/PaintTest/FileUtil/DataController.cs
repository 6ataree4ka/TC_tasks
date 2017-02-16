namespace PaintTest.FileUtil
{
    public static class DataController
    {
        public static string ReadParam(string paramName)
        {
            return Properties.Resources.ResourceManager.GetString(paramName);
        }
    }
}
