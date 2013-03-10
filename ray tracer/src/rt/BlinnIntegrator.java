package rt;

import java.util.Iterator;

import javax.vecmath.Vector3f;

public class BlinnIntegrator implements IntegratorFactory {

	@Override
	public Spectrum integrate(Intersectable scene, LightList lights, Vector3f eye, Ray ray,
			int bounces) {
		HitRecord hitRecord = scene.intersect(ray);
		Spectrum spectrum = new Spectrum(0f, 0f, 0f);
		Iterator<Light> lightIterator = lights.getLightList().iterator();
		if (hitRecord != null && hitRecord.getT() > 0
				&& hitRecord.getT() < Float.POSITIVE_INFINITY) {
			if (hitRecord.getMaterial() != null)
				while (lightIterator.hasNext()) {
					Light light = lightIterator.next();
					spectrum.append(hitRecord.getMaterial().shade(hitRecord, eye, light));
				}
		}
		return spectrum;
	}
}