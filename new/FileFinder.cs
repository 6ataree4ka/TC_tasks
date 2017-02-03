using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace FileFinder
{
    class Program
    {
        static void Main(string[] args)
        {
            // Enter path
            string targetPath = "";
            
            do
            {
                Console.WriteLine("Enter path to folder: ");
                string path = Console.ReadLine();
                // Сделать проверку на OS слешы в разную сторону + Предусмотреть установку дефолтной директории
                if (Directory.Exists(path))
                {
                    targetPath = path;
                }
                else
                {
                    Console.WriteLine("'{0}' is not a valid directory.", path);
                }
            }
            while (targetPath == "");

            // Enter extension
            string targetExt = "";

            do
            {
                Console.WriteLine("Enter file extension: ");
                string ext = Console.ReadLine().Replace(" ", string.Empty);
                if (ext == "")
                {
                    Console.WriteLine("Расширение не может быть пустым.");
                }
                else
                {
                    targetExt = ext;
                }
            }
            while (targetExt == "");

            // Create empty dictiionary where key = filename, value = creation date
            Dictionary<string, DateTime> filesWithCreationDate = new Dictionary<string, DateTime>();

            // Add mask *.ext to find only files with needed extensions
            string[] files = Directory.GetFiles(targetPath, ("*." + targetExt));
            if (files.Length == 0)
            {
                Console.WriteLine("There is no any *.{0} file in {1} folder.", targetExt, targetPath);
                Console.ReadLine();
            }
            else
            {
                foreach (string file in files)
                {
                    string fileName = Path.GetFileName(file);
                    DateTime creationTime = File.GetCreationTime(file);
                    filesWithCreationDate.Add(fileName, creationTime);
                }

                // Sort dictionary by descending
                filesWithCreationDate = filesWithCreationDate.OrderByDescending(x => x.Value).ToDictionary(x => x.Key, x => x.Value);
                
                KeyValuePair<string, DateTime> newer = filesWithCreationDate.First();
                foreach (KeyValuePair<string, DateTime> item in filesWithCreationDate)
                {
                    if ((newer.Value - item.Value).TotalSeconds <= 10)
                    {
                        Console.WriteLine("Target file is {0}, creation date is {1}.", item.Key, item.Value);
                    }
                }
                Console.ReadLine();
            }
        }
    }
}
