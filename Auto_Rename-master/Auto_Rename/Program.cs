using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace Auto_Rename
{
    class Program
    {
        public static string[] name;
        static void Main(string[] args)
        {
            string Path = AppDomain.CurrentDomain.BaseDirectory;
            StreamReader sr = new StreamReader(Path + "/名单.txt", Encoding.UTF8);
            string content;
            while ((content = sr.ReadLine()) != null)
            {
                name = content.Split(',');
            }
            for (int i = 0; i < name.Length; i++)
            {
                int s = i + 1;
                if (File.Exists(Path + "/" + name[i] + ".png"))
                {
                    File.Move(Path + "/" + name[i] + ".png", Path + "/" + s + " " + name[i] + ".png");
                }
                else if (File.Exists(Path + "/" + name[i] + ".jpg"))
                {
                    File.Move(Path + "/" + name[i] + ".jpg", Path + "/" + s + " " + name[i] + ".jpg");
                }
            }
        }
    }
}
