//! Usage: gen-theme <builder.ron> <bundle-config-dir> <bundle-id>
//! Writes <id>.Builder/v2 and <id>.Theme/v2 the way COSMIC computes them.
use cosmic_config::{Config, CosmicConfigEntry};
use cosmic_theme::{Theme, ThemeBuilder};
use std::{env, fs, path::PathBuf};

fn main() {
    let a: Vec<String> = env::args().collect();
    let [_, src, out, id] = &a[..] else { panic!("usage: gen-theme <builder.ron> <config-dir> <id>") };
    let builder: ThemeBuilder = ron::from_str(&fs::read_to_string(src).unwrap()).unwrap();
    let theme: Theme = builder.clone().build();
    write(&builder, "Builder", out, id);
    write(&theme, "Theme", out, id);
}

fn write<T: CosmicConfigEntry + serde::Serialize>(v: &T, part: &str, out: &str, id: &str) {
    let cfg = Config::with_custom_path(&format!("{id}.{part}"), 2, PathBuf::from(out)).unwrap();
    v.write_entry(&cfg).unwrap();
    let _ = fs::remove_dir_all(PathBuf::from(out).join(format!("cosmic/{id}.{part}/v1"))); // with_custom_path creates an empty v1
    let whole = ron::ser::to_string_pretty(v, ron::ser::PrettyConfig::new()).unwrap();
    fs::write(PathBuf::from(out).join(format!("cosmic/{id}.{part}/v2/base")), whole).unwrap();
}
